# spawn

- 父进程会启动一个全新的 python 解释器进程.
- 子进程只继承运行进程对象的 run() 方法所必须的资源.
- 来自父进程的非必须文件描述符和句柄不会被继承.
- 这种方式启动进程最慢.

spawn可在Unix、Windows、MacOS上使用，**它是Windows的默认设置**。





# fork

- 只存在于 Unix  unix中的默认设置   Linux 也是通过这个方式
- 父进程使用 os.fork() 来产生 Python 解释器分叉。子进程在开始时实际上与父进程相同。父进程的所有资源都由子进程继承。请注意，安全分叉多线程进程是棘手的。





# forkserver

程序启动并选择 *forkserver*  启动方法时，将启动服务器进程。从那时起，每当需要一个新进程时，父进程就会连接到服务器并请求它分叉一个新进程。分叉服务器进程是单线程的，因此使用 os.fork() 是安全的。没有不必要的资源被继承。

forkserver可在Unix平台上使用，支持通过Unix管道传递文件描述符。