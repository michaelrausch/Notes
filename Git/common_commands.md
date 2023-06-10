# `git remote add ...` and `git push origin master`

Git is a distributed version control system. Most operations are done locally. To communicate with the outside world, `git` uses what are called `remotes`. These are repositories other than the one on your local disks which can `push` your changes into (so that other people can see them) or `pull` from (so that you can get others changes). The command `git remote add origin git@github.com:...` creates a new remote called `origin` located at `git@github.com`. Once you do this, in your push, push commands, you can push to `origin` instead of typing the whole URL.

- To see the url `origin` is pointing to, use `git remote get-url origin`
- As an experiment, you could use `git remote add puppy https://github.com/Michael-Cowie/test-repo` and then `$git remote get url puppy` will return `https://github.com/Michael-Cowie/test-repo`

# `git push origin master`

This is a command that says "push the commits in the local branch `master` to the remote named `origin`". Once this is executed, all the stuff that you last synchronised with `origin` will be sent to the remote repository and other people will be able to see them.

Now about transports (i.e. what `git://` means). Remote repository URLs can be of many types (`file://`, `https://`). Git simply relies on the authentication mechanism provided by the transport to take care of permissions and stuff. This means that for `file://` URLs, it will be UNIX file permissions etc. The `git://` scheme is asking Git to use its own internal transport protocol, which is optimised for sending git change sets around. As for the exact URL, it's the way it is because of the way github has setup it's `git` server.

# `-u` and `--set-upstream`

`git branch --set-upstream <remote-branch>` sets the default remote branch for the current local branch. Any future `git pull` command (with the current local branch checked-out) will attempt to bring in commits from the `<remote-branch>` into the current local branch.

One way to avoid having to explicitly type `--set-upstream` is to use its shorthand flag `-u` as follows, `$git push -u origin local-branch`. This sets the upstream association for any future `push/pull` attempts automatically. The `-u` option does the following, for every branch that is upto date or successfully pushed, add upstream (tracking) reference, used by the argument-less `git pull` and other commands.

So far pushing your local branch with `-u` option this local branch will be automatically linked with remote branch, and you can use `git pull` without any arguments.