#DSA-Assgn-8
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if(self.__head is None):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if(data_before == None):
            new_node.set_next(self.__head)
            self.__head = new_node
            if(new_node.get_next() == None):
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while(temp is not None):
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while(temp is not None):
            if(temp.get_data() == data):
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if(node is not None):
            if(node == self.__head):
                if(self.__head == self.__tail):
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while(temp is not None):
                    if(temp.get_next() == node):
                        temp.set_next(node.get_next())
                        if(node == self.__tail):
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


class BakeHouse:
    def __init__(self):
        self.__occupied_table_list = LinkedList()

    def get_occupied_table_list(self):
        return self.__occupied_table_list

    def allocate_table(self):
        temp = self.__occupied_table_list.get_head()
        i = 1
        if temp == None:
            self.__occupied_table_list.add(i)
        else:
            while(temp is not None):
                if temp.get_next() is None:
                    self.__occupied_table_list.add(i+1)
                    break
                if i < temp.get_data():
                    self.__occupied_table_list.insert(i, None)
                    break
                if temp.get_next().get_data() != i+1:
                    self.__occupied_table_list.insert(i+1, temp.get_data())
                    break
                temp = temp.get_next()
                i += 1

    def deallocate_table(self, table_number):
        self.__occupied_table_list.delete(table_number)


#Invoke the methods of BakeHouse class and test the program
bakehouse = BakeHouse()

bakehouse.allocate_table()
bakehouse.allocate_table()
bakehouse.allocate_table()
bakehouse.get_occupied_table_list().display()
bakehouse.deallocate_table(2)
bakehouse.get_occupied_table_list().display()
bakehouse.allocate_table()
bakehouse.get_occupied_table_list().display()
