# 每周总结可以写在这里
【树：搜索空间的最佳表示】
	树就是一种典型的二维数据结构。
	这样想，如果链表的next指针不是指向一个节点，而是指向多个节点。例如next->(next1,next2,next….) 那么就变成二维的数据结构了。（也就是多个后继结点）
 
	 树和图最关键的节点是什么？最关键的区别是“有没有环”。也就是有节点指回去。链表是特殊化的树，树就是特殊化的图。
【Python中树的定义】
	class TreeNode:
		def __init__(self,val):
			self.val = val
			self.left, self.right = None,None
	C++ 中树的定义：
	struct TreeNode:
		int val;
		TreeNode *left;
		TreeNode *rignt;
		TreeNode(int x):val(x),left(NULL),right(NULL){}}
【出现树形结构的原因】
	（1）递归：Fibo数列的递归，就是一个树状的节点
	（2）随机状态转移：状态向外扩散选择不同的状态
	注定了搜索算法和树的姻缘——在大的求解空间里找到最优解
	如果树的节点都是无序的，那么就需要遍历。
【树的遍历】
	三句话递归着就可以找，三句话的顺序就是不同的递归方式。
	前序：根-左-右；中序：左-根-右，后序：左-右-根
	【前中后序遍历递归算法原型】
	def preorder(self,root):
		if root:
			self.traverse_path_append(root.val)
			self.preorder(root.left)
			self.preorder(root.right)
	def inorder(self,root):
		if root:
			self.inorder(root.left)
			self.traverse_path_append(root.val)
			self.inorder(root.right)
def postorder(self,root):
		if root:
			self.postorder(root.left)
			self.postorder(root.right)
			self.traverse_path_append(root.val)
class Solution:
    def inorderTraversal(self,root):
        """
        :type root: TreeNode
        :rtype: List[int]
        # 需要定义一个辅助的递归函数
        """
        res = []
        def helper_inorder(root):
            if root:
                helper_inorder(root.left)
                res.append(root.val)
                helper_inorder(root.right) 
        helper_inorder(root)
        return res	为什么基于递归呢？因为树的定义，本身没法有效的进行循环。
	最好的方式是，直接对每个根节点调用相同的遍历函数
	【维护一个栈进行树的遍历】
	为什么可以维护一个栈进行？还是那句话，pop弹出来是栈最重要的操作。实际上前中后序遍历，都需要把前面不符合遍历情况的元素压到栈里面，直到结束才弹出来，这就是栈的思想，实际上递归=栈。
	维护栈，实际上等价于深度优先和广度优先搜素
	案例1：二叉树的前中后层序遍历（栈解决）
	
	案例2：N叉树的前后层序遍历（栈解决）
	
【二叉搜索树】
	遍历一个树就是O(n)的复杂度，那么和一个链表没有太大的区别。二叉搜索树就是排序：要求左子树所有节点都小于根节点，右子树所有节点都大于根节点，且以此类推。中序遍历是一个升序的遍历：
	插入、查询操作都是O(logn)的，这是因为，每次查询节点直接和根节点比较，（首先和根节点比较，比根节点小的话，直接砍掉右边的节点，这里）可以砍掉一半的节点，类似于实现了二分查找——O(log2n)
 
	插入的话也是一样，最后没找到，停下来的地方就是应该插入的地方。
	优点在于插入的操作完全不需要干扰其他任何节点。
	【创建一个二叉搜索树】
	把所有节点依次插入到这个搜索树里面去即可。
	如何插入呢？那么自然是，判断和根节点的大小，然后在左边和右边创建就可以了。
	【删除节点】
	叶子节点直接删掉就可以了；
	根节点的话，不能说把它的子树全部删掉了啊！！应该让一个新节点充当原来的位置！！应该是找一个紧邻根节点但是小于根节点的点&刚刚大于根节点的（右子树里面最小的节点）。题目主要是：二叉树和N叉树的中序遍历
 
	简单讲讲递归和栈的关系：每次递归都是在新开的栈里面压入函数和参数，因为栈秉承后进先出的原则，最里面的肯定是最开始的要解决的函数，因此递归就是栈。
	递归也不见得就比循环差，这个锅不应该递归来背，而是你自己没用缓存把递归写残了。现在的编译器对于递归的优化，都是很高效的。递归的主要是一因为要开一些栈，而不是算法本身上的问题。
	如果要推广到N叉树的话，也可以进行处理：N叉树就没有中了，只有前后和层序遍历：时间复杂度和空间复杂度都是O(n)
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val # 
        self.children = children # 这就是一个列表了
class Solution(object):
    def postorder(self, root):
        res = []
        def helper_postorder(root):
            if root:
                for child in root.children:
                    helper_postorder(child) # 只需要对子节点重复当前操作即可
                    res.append(child.val)
        helper_postorder(root)
        if root:
            res.append(root.val)
        return res
【堆】
	堆是一种能够迅速查找到一堆数当中最大值或者最小值的结构。在实际应用过程中，堆的使用非常普遍，这是因为我可能要按照属性来找出最大值和最小值。
	术语叫“维护”，比如时候任务流，随时要拿出优先级最高的进行处理。
 
实现话也是基于树。
如果要用数组来实现大顶堆的话，那么每次有一个新元素插入进来，首先要进行数组排序，删除的话也是非常麻烦。为什么要用树来进行堆的实现？这就是图灵奖选手考虑的了。
堆的实现有很多种，二叉堆只是因为相对比较好实现，因此被广泛使用。但二叉堆在堆里面算是比较差的。最牛逼的肯定是严格斐波那契堆和2-3堆。但是实现起来很复杂。
【二叉堆性质】
	1、完全树：叶子节点可以不满，但是叶子节点上面肯定的都得是满的；
	2、树中任意节点的值总是≥子节点的值->根节点就是最大的节点->返回根节点值
 
 
	做成树的原因，就是为了让插入删除操作都是O(logn)了。
 
	对于任何一个i，他的左儿子就是2*i+1,例如根节点的话，左儿子就是100和90。完全二叉树以此放进数组。
	插入元素的方法：依次进行交换，先插到最后面，然后慢慢的往上浮动就可以了。怎么浮动呢，只要比他的父亲节点大，那么就和父亲节点交换。这个浮动的操作，最多的是log2n的时间复杂度。
	删除操作（维护）的话，首先就是把最小的元素顶到皇位上面来，依次和自己的儿子作比较。把自己的儿子慢慢的扶上来。
	工程里面，直接用优先队列就可以了。Python当中需要自己写最大和最小堆的函数。
【图】
【图的表示：邻接矩阵和邻接表】
 
	最常见的话肯定是深度优先和广度优先的搜索；visited集合是最大的区别。因为我要标记已经访问过的节点，这是因为：图是有“环”的，我可以按照树的方式去遍历，也就是遍历儿子节点，但是儿子节点一定不能再visited里面：
 
图广度优先算法的模板：
def BFS(graph,start,end):
	queue = []
	queue.append([start])
	visited = set()
	while queue:
		node = queue.pop()
		visited.add(node)
		process(node)
		nodes = generate_relate_nodes(node)
		queue.push(nodes)
	图常考的问题：最短路径，最小生成树，连通图个数，拓扑排序

感想：while 栈不空 pop出来处理是最常见的思想；
最大堆和最小堆的python底层实现是都是列表，因此直接传入构造堆函数即可实现快排，O(nlogn)的时间复杂度
