
class Main {
    public static void main(String[] args) {
        int numAgents = 5;
        Agent[] agents = new Agent[numAgents];

        for(int i = 0; i < numAgents; i++) {
            agents[i] = new Agent(new int[]{i,i+1,i+2, i+3,i+4});
        }

        beginAllocation(agents, numAgents);

        for (Agent agent: agents) {
            System.out.println(agent.getAllocation());
        }
    }
    
    public static int getValuedIndex(int[] values, float target) {
        for (int index = 0; index < values.length; index++) {
            int value = values[index];
            if (value < 0) {
                continue;
            }
            else if ((float) value >= target) {
                return index;
            }
        }

        return -1;
    }

    public static int getMostValuedIndex(int[] values) {
        int maxIndex = 0;
        for (int index = 0; index < values.length; index++) {
            
            if (values[index] > values[maxIndex]) {
                maxIndex = index;
            }
        }
        return maxIndex;
    }

    public static void allocateItem(Agent agent, int index, Agent[] agents) {
        agent.addItemToAllocation(index);
        for (Agent a: agents) {
            a.setItemAsAllocated(index);
        }
    }

    public static void allocationPart1(Agent[] agents, int numAgents) {
        int numAgentsRemaining = numAgents;
        boolean atLeastAgentAllocated = true;
        while (numAgentsRemaining > 0 && atLeastAgentAllocated)  {
            atLeastAgentAllocated = false; 
            for (int i = 0; i < numAgents; i++) {
                Agent agent = agents[i];
                if (!agent.getAllocated()) {
                    float mms = agent.getMMSValue(numAgentsRemaining);
                    float target = mms /2f;
                    int index = getValuedIndex(agent.getValues(), target);
                    if (index != -1) {
                        numAgentsRemaining -= 1;
                        agent.hasBeenAllocated();
                        allocateItem(agent, index, agents);
                        atLeastAgentAllocated = true;
                        continue;
                    }
                }
            }
        }
    }

    public static void allocationPart2(Agent[] agents) {
        while (agents[0].getValueSum() > 0f) {
            for (int agentNum = 0; agentNum < agents.length; agentNum++) {
                Agent agent = agents[agentNum];
                if (!agent.getAllocated()) {
                    if (agent.getValueSum() > 0f) {
                        int maxIndex = getMostValuedIndex(agent.getValues());
                        allocateItem(agent, maxIndex, agents);
                    }
                }
            }
        }
    }

    public static void beginAllocation(Agent[] agents, int numAgents) {
        allocationPart1(agents, numAgents);        
        allocationPart2(agents);
    }
}