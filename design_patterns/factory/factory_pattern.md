The goal of the pattern is to help write code that separates creation from use.

In other words, you should create your objects in a different place than where
you use them.
This is very helpful because then, the code that you write doesn't have to know
anything about how the objects are created when you use them, and that means 
that if in a later stage you decide to change those objects by other objects 
you don't have to change your original code.

What the factory does is that it takes care of the creation for you so that
you can use those objects without knowing the specifics. And the way it works 
is that we need to create an exporter factory that gives us the objects that
we need. 