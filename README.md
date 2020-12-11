# E Magazine Service

The proposed system can be used as an online magazine or a news paper system where the users that subscribe can read posts that are posted by the designated publishers. The posts can have subjects, using which the users can sort the posts if they want to see the earlier posts. The publisher and the subscribers are the two client nodes that are managed by the server functions where the server function uses the RMI API. The posts are further saved using some metadata in a database of the choice so that they can be indexed whenever the user wants to. The account name and the data is also stored in the database so that the authentication could be differentiated for the publishers and subscribers. 


## Implementation Details

You need the [Python3 interpreter](https://www.python.org/downloads/) installed in your system. This is the only dependency.

Once Python is installed and in the system path, open 3 terminal sessions and go to the `src` folder of this project.

Load the server:

```Bash
$ python3 init.py server <host> <port>
```

Load the publisher:

```Bash
$ python3 init.py publisher <server host> <server port>
```

Load the subscriber:

```Bash
$ python3 init.py subscriber <server host> <server port>
```

The server needs a port and a host to expose the API. The clients need the host and the port used by the server.

To start the on-line comunication between server and subscriber, you need to specify the subscriber's location, which will be sent to the server in order establish the connection. The subscriber app will ask for this information in runtime.


## Implementation Screenshots

<img src="https://github.com/therrshan/e-magazine-service/blob/main/Screenshots/1.png" alt="" width="700" height="400">

<img src="https://github.com/therrshan/e-magazine-service/blob/main/Screenshots/2.png" alt="" width="700" height="400">

<img src="https://github.com/therrshan/e-magazine-service/blob/main/Screenshots/3.png" alt="" width="700" height="400">

<img src="https://github.com/therrshan/e-magazine-service/blob/main/Screenshots/4.png" alt="" width="700" height="400">



