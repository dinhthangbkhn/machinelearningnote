# The @property Decorator in Python: Its Use Cases, Advantages, and Syntax

## 1. Advantages of Properties in Python

You can access instance attributes exactly as if they were public attributes while using the "magic" of intermediaries (getters and setters) to validate new values and to avoid accessing or modifying the data directly.

By using @property, you can "reuse" the name of a property to avoid creating new names for the getters, setters, and deleters.

## 2. Don't use @property

``` python
class House:
    def __init__(self, price):
        self.price = price
```

This instance attribute is public because its name doesn't have a leading underscore. Therefore, it can be accessed and modified the attribute directly in other parts of the program using dot notation

``` python
# Access value
obj.price

#Modify value
obj.price = 40000
```

But **if you are asked to make this attribute protected (non-public) and validate the new value before assigning it?**. Use **set** and **get** method to change or get value of price property. You and your team will be panic because each line o code will have to be modified to call the getter and setter.

```python
# Changed from obj.price
obj.get_price()

# Changed from obj.price = 40000
obj.set_price(40000)
```

But... **Properties come to the rescue! With @property**, you and your team **will not need to modify any of those lines** because you will able to add getters and setters "behind the scenes" without affecting the syntax that you used to access or modify the attribute when it was public.

## 3. Property: syntax and logic

```python
class House:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price
```

**Price is now "protected"**: it should not be accessed or modified directly outside of the class. It should only be accessed through intermediaries (getters and setters) if they are available.

## 4. Final tips

You don't necessarily have to define all three methods for every property. You can define read-only properties by only including a getter method. You could also choose to define a getter and setter without a deleter.

If you think that an attribute should only be set when the instance is created or that it should only be modified internally within the class, you can omit the setter.

You can choose which methods to include depending on the context that you are working with.

## Ref

<https://www.freecodecamp.org/news/python-property-decorator/#:~:text=Why%20would%20you%20use%20properties,is%20very%20concise%20and%20readable.&text=By%20using%20%40property%2C%20you%20can,getters%2C%20setters%2C%20and%20deleters>
