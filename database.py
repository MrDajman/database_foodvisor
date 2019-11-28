#!usr/bin/python
# -*- coding: utf-8 -*-

'''
node representation
(child, parent)
'''

class Database:
	
	extract = {}
	status = {}
	updated_parents = [] # list that contains the parents of the nodes that has been added in the update (edit)
	
	def __init__(self, core): # Definig root node. core eg. //("core",None)//
		# Verify if the root node is correct:
		
		self.root_node = core[0]
		self.graph = {None:self.root_node}

	
	def add_nodes(self, new_graph_nodes):
		for new_node in new_graph_nodes:
			if self.parent_exists(new_node[1]):
				self.graph[new_node[1]].append(new_node[0])
			else:
				self.graph[new_node[1]] = [new_node[0]]
			
			if new_node[1] not in self.updated_parents:
				self.updated_parents.append(new_node[1])
		
		
	def add_extract(self, new_extract):
		self.extract.update(new_extract)
		self.updated_parents = []
		
	def get_extract_status(self):
		# loop over the images in extract
		for image, values in self.extract.items():
			print(values)
			print(self.graph)
			if self.is_invalid(values):
				self.status[image] = "invalid"
			elif self.is_coverage_staged(values): #coverage staged has priority over granulity staged
				self.status[image] = "coverage_staged"
			elif self.is_granulity_staged(values):
				self.status[image] = "granularity_staged"
			else: #according to priority
				self.status[image] = "valid"
		
		return(self.status)
		
	
	def parent_exists(self, node):
		return node in self.graph
		
	def is_invalid(self,values):
		''' if node assigned to an image doesn't exist '''
		for value in values:
			values = [val for vals in self.graph.values() for val in vals]
			keys = list(self.graph.keys())
			if value not in values+keys:
				return True
			else:
				False 
	
	def is_coverage_staged(self, values):
		# list containing parents of the nodes
		temp_list = []
		for value in values:
			temp_list.append(self.get_parent(value))
		
		# check if two lists contain the same element
		return(not set(temp_list).isdisjoint(self.updated_parents))
		

	def is_granulity_staged(self, values):
		# check if two lists contain the same element
		return(not set(values).isdisjoint(self.updated_parents))
	
	
	def get_parent(self, search_node):
		for parent, nodes in self.graph.items():
			for node in nodes:
				if node == search_node:
					return parent
					

