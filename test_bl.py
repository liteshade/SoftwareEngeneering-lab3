import pytest
from main import generate_directed_graph
from graph import Graph
@pytest.fixture
def graph():
    filename = "file/test5.txt"  # 文件名
    graph = Graph()  # 创建一个有向图对象
    generate_directed_graph(graph, filename)  # 生成有向图
    return graph

# 无效等价类测试用例
def test_word1_not_in_graph(graph):
    assert graph.query_bridge_words("not_in_graph", "any_word") == "No not_in_graph or any_word in the graph!"

def test_word2_not_in_graph(graph):
    assert graph.query_bridge_words("any_word", "not_in_graph") == "No any_word or not_in_graph in the graph!"

def test_word1_and_word2_not_in_graph(graph):
    assert graph.query_bridge_words("an", "exciting") == "No an or exciting in the graph!"

def test_no_input_graph(graph):
    assert graph.query_bridge_words(" ", " ") == "No   or   in the graph!"


# 有效等价类测试用例
def test_single_bridge_word(graph):
    # 假设测试文件中有 "a -> b -> c"
    assert graph.query_bridge_words("explore", "new") == "The bridge words from explore to new is: strange."

def test_multiple_bridge_words(graph):
    # 假设测试文件中有 "a -> b -> d" 和 "a -> c -> d"
    assert graph.query_bridge_words("new", "and") == "The bridge words from new to and are: life, live." or "The bridge words from new to and are: live, blife."

def test_no_bridge_words(graph):
    # 假设测试文件中没有从 "a" 到 "d" 的桥接词
    assert graph.query_bridge_words("seek", "to") == "No bridge words from seek to to!"


# 边界值测试用例
def test_no_word_in_graph():
    no_word_graph = Graph()
    assert no_word_graph.query_bridge_words(" ", " ") == "No   or   in the graph!"


def test_single_word_in_graph():
    single_word_graph = Graph()
    single_word_graph.nodes.add("onlyword")
    assert single_word_graph.query_bridge_words("onlyword", "onlyword") == "No bridge words from onlyword to onlyword!"

def test_two_words_in_graph():
    two_words_graph = Graph()
    two_words_graph.add_edge("first", "second", 1)
    assert two_words_graph.query_bridge_words("first", "second") == "No bridge words from first to second!"