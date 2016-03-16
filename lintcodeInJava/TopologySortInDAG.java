
/*Topological Sorting:

Requirement:
1: Directed Acyclic Graph (DAG). 非DAG图没有拓扑排序一说
2: Every Node apear only once(每个顶点出现且只出现一次)

Application: 拓扑排序通常用来“排序”具有依赖关系的任务。
比如，如果用一个DAG图来表示一个工程，其中每个顶点表示工程中的一个任务，用有向边 表示在做任务 B 之前必须先完成任务 A。
故在这个工程中，任意两个任务要么具有确定的先后关系，要么是没有关系，绝对不存在互相矛盾的关系（即环路）

Method:有两种方法： kahn 和 dfs
*/


////////////////////////////////////////////////////
//kahn 算法：关键在于需要维护一个入度为0的顶点的集合
/* 
1: 图中节点的表示，将每个节点进行编号，例如0～V, V代表是节点的个数，
2: 使用邻接表来存储有向图的信息，即整个adj[] 数组内每个元素是个arraylist的引用 即 
		ArrayList<Integer>[] res = new ArrayList[5];
		for(int i=0;i<res.length;i++) //初始化
		{
			res[i] = new ArrayList<Integer>();
		}
3: 每个节点有一个变量－入度(indegrees),当indgrees为0时，代表没有节点指向该节点，
由于步骤1已经对节点进行编号了，因此使用一个整形数组即可，下标对应的是节点。
4: 使用集合来存储入度为0的节点的集合，可以是stack/queue,具体的数据结构可以根据不同题目要求来指定
5: 使用一个变量来 count 或者 edge来记录图是否已经排序完，当入度为0的集合为空但我们还没输出完整个图时，我们即可判断原图不是DAG的。
*/

//参考代码： http://blog.csdn.net/dm_vincent/article/details/7714519
public class KahnTopological  
{  
    private List<Integer> result;   // 用来存储结果集  
    private Queue<Integer> setOfZeroIndegree;  // 用来存储入度为0的顶点  
    private int[] indegrees;  // 记录每个顶点当前的入度  
    private int edges;  
    private Digraph di;  
      
    public KahnTopological(Digraph di)  
    {  
        this.di = di;  
        this.edges = di.getE();  
        this.indegrees = new int[di.getV()];  
        this.result = new ArrayList<Integer>();  
        this.setOfZeroIndegree = new LinkedList<Integer>();  
          
        // 对入度为0的集合进行初始化  
        Iterable<Integer>[] adjs = di.getAdj();  
        for(int i = 0; i < adjs.length; i++)  
        {  
            // 对每一条边 v -> w   
            for(int w : adjs[i])  
            {  
                indegrees[w]++;  
            }  
        }  
          
        for(int i = 0; i < indegrees.length; i++)  
        {  
            if(0 == indegrees[i])  
            {  
                setOfZeroIndegree.enqueue(i);  
            }  
        }  
        process();  
    }  
      
    private void process()  
    {  
        while(!setOfZeroIndegree.isEmpty())  
        {  
            int v = setOfZeroIndegree.dequeue();  
              
            // 将当前顶点添加到结果集中  
            result.add(v);  
              
            // 遍历由v引出的所有边  
            for(int w : di.adj(v))  
            {  
                // 将该边从图中移除，通过减少边的数量来表示  
                edges--;  
                if(0 == --indegrees[w])   // 如果入度为0，那么加入入度为0的集合  
                {  
                    setOfZeroIndegree.enqueue(w);  
                }  
            }  
        }  
        // 如果此时图中还存在边，那么说明图中含有环路  
        if(0 != edges)  
        {  
            throw new IllegalArgumentException("Has Cycle !");  
        }  
    }  
      
    public Iterable<Integer> getResult()  
    {  
        return result;  
    }  
} 

///////////////////////////////////////////////////////
//dfs 算法： 递归遍历整个图，然后标记访问过的节点，在dfs结束后加入节点到结果中
/*
1: 使用stack来记录结果，dfs记录的记过是逆序的结果
2: 使用visited[]数组来标记每个节点是否被访问了
*/

// 参考解释： http://blog.csdn.net/dm_vincent/article/details/7714519

public class DirectedDepthFirstOrder  
{  
    // visited数组，DFS实现需要用到  
    private boolean[] visited;  
    // 使用栈来保存最后的结果  
    private Stack<Integer> reversePost;  
  
    /** 
     * Topological Sorting Constructor 
     */  
    public DirectedDepthFirstOrder(Digraph di, boolean detectCycle)  
    {  
        // 这里的DirectedDepthFirstCycleDetection是一个用于检测有向图中是否存在环路的类  
        DirectedDepthFirstCycleDetection detect = new DirectedDepthFirstCycleDetection(  
                di);  
          
        if (detectCycle && detect.hasCycle())  
            throw new IllegalArgumentException("Has cycle");  
              
        this.visited = new boolean[di.getV()];  
        this.reversePost = new Stack<Integer>();  
  
        for (int i = 0; i < di.getV(); i++)  
        {  
            if (!visited[i])  
            {  
                dfs(di, i);  
            }  
        }  
    }  
  
    private void dfs(Digraph di, int v)  
    {  
        visited[v] = true;  
  
        for (int w : di.adj(v))  
        {  
            if (!visited[w])  
            {  
                dfs(di, w);  
            }  
        }  
  
        // 在即将退出dfs方法的时候，将当前顶点添加到结果集中  
        reversePost.push(v);  
    }  
  
    public Iterable<Integer> getReversePost()  
    {  
        return reversePost;  
    }  
}