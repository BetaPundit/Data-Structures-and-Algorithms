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
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while(temp is not None):
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while(temp is not None):
            if data == temp.get_data():
                return temp
            temp = temp.get_next()
        return None

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            # self.__head.set_next(new_node)
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node
        else:
            node_before = self.find_node(data_before)
            new_node.set_next(node_before.get_next())
            node_before.set_next(new_node)
            if new_node.get_next is None:
                self.__tail = new_node

    def delete(self, data):
        found_node = self.find_node(data)
        if found_node:
            if self.__head == found_node:
                self.__head = found_node.get_next()
                if self.__tail == found_node:
                    self.__tail = None
            else:
                temp = self.__head
                while(temp is not None):
                    if temp.get_next() == found_node:
                        break
                    temp = temp.get_next()
                temp.set_next(found_node.get_next())
                if found_node == self.__tail:
                    self.__tail = temp
                found_node.set_next(None)
        else:
            print('Not Found!')

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


list1 = LinkedList()
# Add all the required element(s)
list1.add("Sugar")
list1.add("Milk")

# list1.add(1)
# list1.add(2)
# list1.add(3)
# list1.add(4)
# list1.add(5)
list1.display()
# Delete the required element.
list1.delete("Sugar")
list1.display()


# def fun(head):
#     if(head == None):
#         return
#     if head.get_next().get_next() != None:
#         print(head.get_data(), " ", end='')
#         fun(head.get_next())
#     print(head.get_data(), " ", end='')


# fun(list1)
