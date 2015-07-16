import java.util.ArrayList;



public class Simulation {
	private ArrayList<ArrayList<Node>> Grid = new ArrayList<ArrayList<Node>>();
    
	public Simulation() {
		// TODO Auto-generated constructor stub
		
	}
	

	public boolean makeGrid(int n)	{
        
		for(int i = 0; i < n; i++)	{
			ArrayList<Node> list = new ArrayList<Node>();
			Grid.add(list);
            
			for(int j = 0; j < n; j++)	{
				Node object = new Node();
				Grid.get(i).add(object);
			}
		}
		return true;
	}
	public boolean populateNeighbors(){
        
		for(int counter1=0; counter1<Grid.size();counter1++){
            
			for (int counter2=0; counter2<Grid.get(0).size(); counter2++){
				ArrayList<Node> neighborshello=new ArrayList<Node>();
                
				if (((counter1!=0)&&(counter1!=(Grid.size()-1)))&&(counter2!=0)&&(counter2!=(Grid.get(0).size()-1))){
					neighborshello.add(Grid.get(counter1).get(counter2+1));
					neighborshello.add(Grid.get(counter1).get(counter2-1));
                    
					if (counter1%2>0){
						neighborshello.add(Grid.get(counter1-1).get(counter2));
					}
                    else if (counter1%2==0){
						neighborshello.add(Grid.get(counter1+1).get(counter2));
					}
                    
					System.out.println(neighborshello);
					Grid.get(counter1).get(counter2).neighbors=neighborshello;
					continue;
				}
                
				if((counter2+1)<Grid.get(counter1).size()){
					neighborshello.add(Grid.get(counter1).get(counter2+1));
				}
                
				if ((counter2-1)>=0){
					neighborshello.add(Grid.get(counter1).get(counter2-1));
				}
                
				if ((counter1==0)&&(counter2==0)){
					System.out.println(neighborshello);
					Grid.get(counter1).get(counter2).neighbors=neighborshello;
					continue;
				}
                
				if ((counter1==0)&&(counter2==(Grid.get(counter1).size()-1))){
					if (counter2%2==0){
						System.out.println(neighborshello);
						Grid.get(counter1).get(counter2).neighbors=neighborshello;
						continue;
					}
                    else {
						neighborshello.add(Grid.get(counter1+1).get(counter2));
						System.out.println(neighborshello);
						Grid.get(counter1).get(counter2).neighbors=neighborshello;
						continue;
					}
				}
                
				if ((counter2==0)&&(counter1==(Grid.size()-1))){
					if (counter1%2==0){
						neighborshello.add(Grid.get(counter1-1).get(counter2));
						System.out.println(neighborshello);
						Grid.get(counter1).get(counter2).neighbors=neighborshello;
						continue;
					}
                    else {
						System.out.println(neighborshello);
						Grid.get(counter1).get(counter2).neighbors=neighborshello;
						continue;
					}
				}
                
				if ((counter1==(Grid.size()-1))&&(counter2==(Grid.get(counter1).size()-1))){
					neighborshello.add(Grid.get(counter1-1).get(counter2));
					System.out.println(neighborshello);
					Grid.get(counter1).get(counter2).neighbors=neighborshello;
					continue;
				}
                
				if (counter1%2==0){
					try{
					neighborshello.add(Grid.get(counter1-1).get(counter2));
					System.out.println(neighborshello);
					Grid.get(counter1).get(counter2).neighbors=neighborshello;
					continue;
					}
					catch (IndexOutOfBoundsException e){
						continue;
					}
                    
				}
				if (counter1%2!=0){
					try {
					neighborshello.add(Grid.get(counter1+1).get(counter2));
					System.out.println(neighborshello);
					Grid.get(counter1).get(counter2).neighbors=neighborshello;
					continue;
					} 
					catch (IndexOutOfBoundsException e){
						continue;
					}
				}
			}
		}
		return true;
	}
    
	public static void main(String[] args) {
		Simulation k = new Simulation();
		System.out.println(k.makeGrid(100));
		System.out.println(k.populateNeighbors());
	}

}