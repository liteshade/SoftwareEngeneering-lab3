'''
模块用以测试
'''
import pytest
from main import generate_directed_graph
from graph import Graph

filename = "file/test5.txt"  # 文件名
my_graph = Graph()  # 创建一个有向图对象
generate_directed_graph(my_graph, filename)  # 生成有向图

# Test cases based on the provided paths
@pytest.mark.parametrize("word1, word2, nodes, edges, expected1, expected2", [
    # Path 1: word1 或 word2 不在图中
    ("apple", "banana",None,None, "No apple or banana in the graph!",False),
    ("orange", "grape",None,None, "No orange or grape in the graph!",False),
    (" ", " ",None,None, "No   or   in the graph!",False),

    # Path 2: 图中只有 word1 和 word2 两个单词
    ("cat", "dog", {"cat", "dog"}, {}, "No bridge words from cat to dog!",False),
    ("tree", "bush", {"tree", "bush"}, {}, "No bridge words from tree to bush!",False),

    # Path 3: 检查所有节点，没有桥接词
    ("seek", "to" ,None,None, "No bridge words from seek to to!",False),
    ("to", "explore" ,None,None, "No bridge words from to to explore!",False),

    # Path 4: 恰好找到一个桥接词
    ("explore", "new" ,None,None, "The bridge words from explore to new is: strange.",False),
    ("life", "new" ,None,None, "The bridge words from life to new is: and.",False),

    # Path 5: 找到多个桥接词
    ("new", "and",None,None, "The bridge words from new to and are: life, live.","The bridge words from new to and are: live, life."),
    ("rain", "shine", 
     {"rain", "and", "thunder", "shine"},
     {("rain", "and"), ("and", "shine"), ("rain", "thunder"), ("thunder", "shine")},
     "The bridge words from rain to shine are: and, thunder.","The bridge words from quick to fox are: thunder, and."),

    # Path 6: 找到多个桥接词并再次遍历部分节点
    ("first", "last", 
     {"first", "middle1", "middle2", "last"},
     {("first", "middle1"), ("middle1", "middle2"), ("middle2", "last"), ("first", "middle2"), ("middle1", "last")},
     "The bridge words from first to last are: middle1, middle2.",
     "The bridge words from first to last are: middle2, middle1."),
    
    ("begin", "end", 
     {"begin", "halfway", "almost", "end"},
     {("begin", "halfway"), ("halfway", "almost"), ("almost", "end"), ("begin", "almost"), ("halfway", "end")},
     "The bridge words from begin to end are: halfway, almost.","The bridge words from begin to end are: almost, halfway."),

])
def test_query_bridge_words(word1, word2, nodes , edges, expected1, expected2):
    if nodes == None:
        graph = my_graph
    else:
        graph = Graph()
        graph.edges = edges
        graph.nodes = nodes
    assert graph.query_bridge_words(word1, word2) == expected1 or expected2
