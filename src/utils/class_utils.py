from typing import Type, Union, Optional, Sequence, TypeVar, Generic

T = TypeVar("T")


class ClassUtils(Generic[T]):
    @staticmethod
    def is_the_same_class(cls1: Type, cls2: Type) -> bool:
        """判断两个类是否相同

        由于使用的是插件的导入方式，所以使用isinstance判断会有问题，需要使用这种方式判断
        """
        if (
            cls1.__name__ == cls2.__name__
            and cls1.__module__.split(".")[-1] == cls2.__module__.split(".")[-1]
        ):
            return True
        return False

    @staticmethod
    def tran_obj2type(obj: Union[Type, object]) -> Type:
        """将实例化之后的类对象转换成类型，如果本来就是类型则不转换"""
        if isinstance(obj, type):
            return obj
        return type(obj)

    @staticmethod
    def get_obj_in_list_by_type(
        search_type: Type, search_list: Sequence[T]
    ) -> Optional[T]:
        for obj in search_list:
            if ClassUtils.is_the_same_class(search_type, type(obj)):
                return obj
        return None


if __name__ == "__main__":
    print(ClassUtils.is_the_same_class(int, int))
