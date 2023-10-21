def oxford_comma(items):
    if (items == None): return None;
    elif (len(items) < 1): return "";
    elif (len(items) == 1): return items[0];
    else: pass;
    myjnitems = [];
    for i in range(len(items) - 1):
        myjnitems.append(items[i]);
    mycmaspcstr = ", ";
    myjnstr = mycmaspcstr.join(myjnitems);
    #print(f"myjnstr = {myjnstr}");
    if (len(items) == 2): return myjnstr + " and " + items[len(items) - 1];
    else: return myjnstr + mycmaspcstr + "and " + items[len(items) - 1];

#oxford_comma(["Tron", "Alan", "Clu", "Kevin Flynn"]);
