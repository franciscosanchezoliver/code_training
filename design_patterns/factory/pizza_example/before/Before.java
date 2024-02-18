package before;

public class Before {

    public Before() {

    }

    Pizza orderPizza(String type) {
        Pizza pizza = null;

        if (type.equals("cheese")) {
            pizza = new CheesePizza();
            System.out.println("Cheese pizza created");

        } else if (type.equals("greek")) {
            pizza = new GreekPizza();
            System.out.println("Greek pizza created");
        } else if (type.equals("pepperoni")) {
            pizza = new PepperoniPizza();
            System.out.println("Pepperoni pizza created");
        }

        return pizza;
    }

    public static void main(String[] args) {
        System.out.println("hola");
        Before before = new Before();
        before.orderPizza("cheese");
    }

}
