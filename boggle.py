#! /usr/bin/python3

import sys
import time
import boggle_graph

letters = sys.argv[1]
n = int(sys.argv[2])
if len(sys.argv) == 4:
	wordlist = sys.argv[3]
else:
	print["You must include a dictionary"]

def create_dictionary(dic):
	try:
		f = open(dic, 'r')
		return {line.strip().lower() for line in f.readlines()}
	except IOError:
		sys.exit()

def dfs(visited_nodes, graph, node=('', (None, None))):
	global dictionary
	visited_nodes = visited_nodes + [node]
	word_fragment = "".join([letter for letter, position in visited_nodes])

	if len(word_fragment) >= 3 and word_fragment in dictionary:
	    yield word_fragment

	good_neighbors = [n for n in graph[node] if n not in visited_nodes]

	for neighbor in good_neighbors:
		for result in dfs(visited_nodes, graph, neighbor):
			yield result

if __name__ == "__main__":
	start = time.time()
	dictionary = create_dictionary(wordlist)
	print("dictionary created")

	board, position = boggle_graph.make_board(letters, n)
	graph = boggle_graph.make_graph(board, position)
	words_out = []
	for word in dfs([], graph):
		words_out.append(word)
	
	end = time.time()
	timer = end - start
	print("All the", len(words_out), "word are:",*words_out, sep=', ')
	
	if timer >= 60:
		timer = timer/60
		print("it take {:.2f}".format(timer), "Minutes")
	elif timer >= 3600:
		timer = timer/3600
		print("it take {:.2f}".format(timer), "Hours")
	else:
		print("it take {:.2f}".format(timer), "seconds")