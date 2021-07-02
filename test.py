print("hello world")
print("second commit")

"""
In a particular git repo you can make changes to files
git add .  # adds all changes to be committed
git commit -m "commit message" # commits it on that current branch
git checkout is for switching branches

after making a repo on github.com once logged in,
a local git repo can be assigned a remote origin ( the website you want to upload your project onto on github)
in this case

git remove add origin "https://github.com/sz830/test.get" # this sets the current repos "remote origin" to what url you give it.
Future push and pull requests to origin will look at this url. master is the branch.

Can see this new remote origin setting in
git config --local --edit # lets you edit local repo git config file.
Different projects will want different remote repos to push and pull from.

Lets say we want to push our changes, our commits and everything onto the remote origin.
git push -u origin master # -u means upstream, origin means push to our remote origin, master means which branch of our remote origin. in this case, master.
If there's error, maybe you aren't connected to internet.
Should make you sign in the first time.

Lets say we wanna pull a repo onto our computer somehow.
git init # so git commandds work.
git pull "https://github.com/sz830/test.git" master # will get what's on github and put it in your current directory

pulling from a remote origin DOES NOT make that origin your local remote origin when you push.
you have to set it first if you wanna be able to push to that place too.
"""