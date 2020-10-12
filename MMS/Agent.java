import java.util.ArrayList;

public class Agent {
    private int[] values;
    private ArrayList<Integer> allocation;
    private boolean allocated;

    public Agent(int[] values) {
        this.values = values;
        this.allocation = new ArrayList<Integer>();
        this.allocated = false;
    }

    public void hasBeenAllocated() {
        this.allocated = true;
    }

    public ArrayList<Integer> getAllocation() {
        return this.allocation;
    }

    public boolean getAllocated() {
        return this.allocated;
    }

    public int[] getValues() {
        return this.values;
    }

    public void setItemAsAllocated(int index) {
        this.values[index] = -1;
    }

    public float getMMSValue(int numAgents) {
        float sum = this.getValueSum(); 
        return sum / numAgents;
    }

    public float getValueSum() {
        int sum = 0;
        for(int val: this.values) {
            if (val != -1) {
                sum += val;
            }
        }
        return sum;
    }

    public void addItemToAllocation(int itemNum) {
        allocation.add(itemNum);
    }
}
