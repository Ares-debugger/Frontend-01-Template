# 每周总结可以写在这里
【深度优先搜索】
【递归写法代码模板】
	def dfs(node):
		if node in visited: # 终止条件
			return 
		visited.add(node)
		dfs(node.left)
		dfs(node.right)
	多叉树情况也是如此：
	def dfs(node):
		if node in visited: # 终止条件
			return 
		visited.add(node)
		for next_node in node.children():
			if not next_node in visited:
				dfs(next_node,visited)
	# 注意这里要传入visited带入下一层，并且不会等这个循环走完就直接进入下一	层孩子节点里面去。实际上是一个回溯的算法。
【非递归写法代码模板】
	手动维护一个栈：
	def DFS(self,tree):
		if tree.root is None:
			return []
		visited, stack = [],[tree.root]
		while stack:
			node = stack.pop()
			visited.add(node)
			process(node)
			nodes = generate_related_nodes(node)
			stack.push(nodes)
理解深度优先搜索：先把节点放进去，再把儿子节点放进去，直到最后一个节点都进去，才开始往外面拿，拿从叶子节点开始拿，然后最后才到根节点。
【广度优先搜索】
	广度优先遍历就不再是用递归或者是栈了，而是用队列。广度优先比较符合人脑搜索的习惯，并且在求取最短路径问题当中有较好的实现。
【广度优先代码模板】
	def BFS(graph,start,end):
		queue = [] # 也可以用collections里面的deque结构
		queue.append([start])
		visited.add(start)
		while queue:
			node = queue[0]
			queue.remove(node)
			visited.add(node)
			process(node)
			nodes = generate_related_nodes(node) # 扩散出周围节点依次加入队列
			queue.push(nodes) # 先入先出，实现广度优先
理解广度优先：先把根节点放进去，根节点随后出来，然后把所有儿子节点放进去，儿子节点依次出来，再把孙子节点放进去，孙子节点依次出来。
案例1：二叉树的层序遍历
首先，广度优先搜索，可以解决这个问题，那么为了完整性，深度优先搜索也可以解决这个问题。为什么呢，因为广度优先搜索势必要解决一个“当前是哪一个层”的问题，但是深度优先搜索可以标记出来哪个层。因为每次有level嘛。
广度优先解法：其实是难以标记层级的。队列中会同时存在上一层和下一层的节点，并且紧挨在一起。这样的话，就需要修改代码为，每次出的都是一层，而不是混杂在一起的。方法为：在每一层开始遍历之前，先记录队列中的节点数量n：也就是这一层的节点数量，然后一口气处理完这一层的n个节点。
就以一个3,7,9为例。第一次循环，队列里面只有3这一个节点，那么取queue[0]->3，两个子节点7和9进入队列
队列长度为2，这个时候遍历，实际上node[0]两次分别就取出了7和9,
当然7和9下面也会有子节点，但是我每次取出node[0]，就会是这一层的所有数字。慢慢的体会入队和出队的顺序问题。
 
	深度优先搜索怎么做呢，实际上就是记录下当前的层的信息，提取出来，维护一个哈希表，把对应的level加进去就可以了。我们只需要更简单的使用列表，连hashmap都不要：
 
	一旦遍历的层数大于当前的res中列表的个数了，我就要增加一个空列表，防止下标越界。
案例2：岛屿数量（理解CV式递归）
	这个题是一个典型的CV题，应该要好好的训练。深度优先搜索，怎么做呢？首先，遍历所有节点，一旦找到一个1，那么岛屿数量+1，而后，把和这个1相连的其他1（上下左右）全部打掉。夷为平地变成0。直到循环到最末尾，全部都为0了，那么说明把这个岛统计完了。
    def numIslands(self, grid):
        count = 0
        self.height = len(grid)
        self.width = len(grid[0])
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == '1':
                    count+=1
                    self.mark(grid,i,j)
        return count

    def mark(self,grid,i,j):
        '''
        :param grid: 传进来的棋盘
        :param i: 遍历的i坐标
        :param j: 遍历的j坐标
        :return:
        '''
        # teminator 设置一些直接跳过的情况
        # 当前虽然不可能出现越界，但是递归会把i和j进行更新，变为i和j的l邻域 
       # 理解这种执行完再回过来的递归顺序很重要
        if i<0 or j<0 or i>=self.height or j>=self.width or grid[i][j]=='0':
            return None # 传入的参数是这种情况的话，直接跳过，这是非常常见递归处理
        else:
            # process
            grid[i][j] = '0'
            self.mark(grid,i-1,j)
            self.mark(grid,i+1,j)
            self.mark(grid,i,j-1)
            self.mark(grid,i,j+1)
【优先级搜索】
【贪心算法】
	贪心算法是每一步寻找当前的最优结果，因此可能陷入局部最优。
	贪心算法和动态规划的不同在于它对每个子问题的解决方法都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。
	如果能回退的话，就是回溯，或者最优判断+回退。
	贪心算法可以解决一些最优化问题。
	这里面要注意两个点：
	（1）一旦贪心法能够解决某一个问题，那么基本上是这个问题所有解法中最好的；
	（2）贪心法虽然不能完全解决某些问题，但是可以作为一个近似的辅助解法
【什么时候能够用贪心算法】
简单的说，问题能够分解为子问题来解决，子问题的最优解能够地推到最终问题的最优解。这种子问题最优解称为最优子结构。
案例1：分发饼干问题
		排序之后，用最小的饼干去满足最小的胃口。
		从小到大匹配两个数组
案例2：最佳买卖股票的时机。
		如果第二个数字比第一个大的话，就正常即可。
案例3：跳跃游戏
		按照数组进行跳跃，能不能调到最后一个。从后往前进行贪心。
【二分查找】
【三大条件】
	1、单调性；2、上下界；3、索引（可以用下标进行访问）
【代码模板】
	left,right = 0, len(array)-1
	while left < right:
		mid = (left+right)/2
		if array[mid]==target:
			break or return result
		elif array[mid]<target:
			left = mid +1
		else:
			right = mid -1
案例1：求平方根（只保留整数部分）
首先，为什么能用二分查找，这是因为在查找区域里面（0，x）里面，是有界的，因为平方根一定在（0，x）这个区间里面。并且，可以使用索引查找到。这里直接做就可以了。直接套二分查找模板。
牛顿迭代法。用直线代替曲线。x无限这个函数的值。
案例2：判断一个数是否是完全平方数
案例3：搜索旋转排序数组
		这个题困难的地方就在于，单调性被破坏了。破坏了之后如何去找呢？
