README.md

#Bellman Ford Distance Vector Routing Protocol

##Use

Everything needs to be entered manually for each node
In the future I would like to use a better io method.

##Better io how to implement io:
    pretend that the graph is complete
        nodes that arent connected get 0 weight
        basically have an external file with a square of numbers
    litearlly go though the lines:
        the len of the line is the size of the graph
        go through each n in the line:
            if n is 0 ignore
            if n != 0:
                add index of n to neighbor list
                add n to neighbor weights
    done