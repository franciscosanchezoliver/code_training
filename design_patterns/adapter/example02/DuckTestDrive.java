
public class DuckTestDrive {

    public static void main(String[] args) {

        // Creation of a real Duck, the mallard duck.
        MallardDuck duck = new MallardDuck();

        System.out.println("A Duck can 'quack' and 'fly'");
        duck.quack();
        duck.fly();

        // We also have turkeys, we can create a Wild turkey
        WildTurkey turkey = new WildTurkey(3);

        System.out.println("A turkey can 'gobble' and 'fly'");
        turkey.gobble();
        turkey.fly();

        // But imagine that we want to use a turkey like a duck. In that case
        // we need the turkey to be able to "quack" instead of "gobble".
        // To do this, we can create an Adapter class.
        Duck turkeyAsDuck = new TurkeyAdapter(turkey);

        System.out.println("A turkey adapter can 'quack' and 'fly'");
        turkeyAsDuck.quack();
        turkeyAsDuck.fly();

    }

}