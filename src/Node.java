import java.util.ArrayList;


public class Node extends Simulation {
	double atomchargeproportion;
	int hybridization;
	int heat;
	ArrayList<Node> neighbors=new ArrayList<Node>();
	ArrayList<Node> externalconnections=new ArrayList<Node>();
	public Node(double atomchargeproportion,int hybridization,int heat)	{
		this.atomchargeproportion = atomchargeproportion;
		this.hybridization = hybridization;
		this.heat = heat;
	}
	public Node() {
		// created constructor for Node
	}
}
