#### Create a map-reduce job

----

<pre>
    [
        {
            "name":"mapper",
            "exec":{"path":"swift://my_account/exec/maper.nexe"},
            "devices":[
                {"name":"stdin","path":"swift://my_account/data/binary*.data"},
                {"name":"stderr"}
            ],
            "connect":["mapper","reducer"]
    },
        {
            "name":"reducer",
            "exec":{"path":"swift://my_account/exec/reducer.nexe"},
            "connect":["manager"],
            "count":5
    },
        {
            "name":"manager",
            "exec":{"path":"swift://my_account/exec/manager.nexe"},
            "devices":[
                {"name":"stdout","path":"swift://my_account/data/mapred_result.data"},
                {"name":"stderr"}
            ]
    }
    ]
</pre>

- This one uses networking, `connect` property is set on some nodes.
- Mappers are connected to mappers (between themselves) and to reducers.
- Each `connect` means unidirectional connect, i.e. each mapper can send to each other mapper and to each reducer.
- Each reducer can send only to manager node.
- Manager node has no `count` and its `devices` has no wild-cards, means there is exactly _one_ manager node.
- There are 5 reducers: `count: 5`.
- There are N mappers, it depends how many objects match the `swift://my_account/data/binary*.data` wildcard.
If there are 10 matching objects, there will be 10 mappers, each mapper will have 9 connections to 9 other mappers and 5 connections to each reducer.
- Each mapper will see something like this in its /dev/in/ directory:
    <pre>
    mapper-1
    mapper-2
    mapper-3
    mapper-4
    ........
    </pre>
    In /dev/out/ directory:
    <pre>
    mapper-1
    mapper-2
    mapper-3
    mapper-4
    ........
    reducer-1
    reducer-2
    ........
    </pre>
- The own node name can be found by reading `argv[0]` parameter (i.e. executable name).
Using its own name from `argv[0]` and names of all other connected nodes from traversing /dev/in and /dev/out, each node can have full network map of all nodes it needs to communicate with.
