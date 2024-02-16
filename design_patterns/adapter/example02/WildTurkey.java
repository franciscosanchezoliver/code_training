public class WildTurkey implements Turkey {

    private int age = 0;

    public WildTurkey(int age) {
        this.age = age;
    }

    @Override
    public void gobble() {
        System.out.println("Gobble Gobble");
    }

    @Override
    public void fly() {
        System.out.println("I'm flying a short distance");
    }

}
