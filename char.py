# Initiate dcitionary of lists with syntax sets. Default is syntax

        #Common Syntax Characters
list_ = {"syntax": 
            [ "*","(",")","_","+",
            "{","}","|","[","]","\\",
            ":",'"',"'",";","'",
            "<",">","?",",",".","?",
            "%","#","!","~","`","^","&" 
            ],

        #Common git Commands            
        "git" :
            ['cd', 'cd ../', 'cd ~', 'code', 'conda activate', 'cp', 'echo', 
             'git add .', 'git branch', 'git checkout', 'git clone', 'git commit -m', 
             'git config', 'git diff', 'git fetch', 'git init', 'git log', 'git log', 
             'git log', 'git merge', 'git mv', 'git pull', 'git push', 'git rebase', 
             'git rebase', 'git remote add', 'git reset', 'git rm', 'git show', 
             'git stash', 'git status', 'jupyter lab', 'ls', 'mkdir', 'mv', 'pwd', 
             'python', 'touch'
            ],
        
        # Common python functions
        "python":
            ['!=', '%=', '*=', '+=', '-=', '/=', '<=', '==', '>=', 
             '.append', '.discard', '.format', '.get', '.insert', 
             '.intersection', '.pop', '.remove', '.remove', '.setdefault', 
             '.sort', '.union', '.update', '.values', 
             'False', 'True', 'add', 'and', 'break', 'def', 'del', 'difference', 
             'elif', 'else', 'end', 'float', 'for', 'from', 'if', 'import', 'in', 
             'input', 'int', 'is', 'is not', 'lambda', 'len', 'list', 'map', 'or', 
             'pass', 'print', 'range', 'return', 'reverse', 'sep', 'set', 'sorted()', 
             'str', 'tuple', 'type', 'while', 'zip'
            ],
        
        #Common PANDAS functionality
        "pandas":
            ['.DataFrame', '.DataFrame', '.Series', '.append', '.apply', '.astype', 
             '.columns', '.concat', '.corr', '.count', '.describe', '.describe', '.dropna', 
             '.fillna', '.groupby', '.head', '.index=', '.info', '.isnull', '.join', '.max', 
             '.mean', '.median', '.merge', '.min', '.notnull', '.pivot', '.read_clipboard', 
             '.read_csv', '.read_excel', '.read_html', '.read_json', '.read_sql', 
             '.read_table', '.rename', '.replace', '.set_index', '.shape', '.shift', 
             '.sort_index', '.sort_values', '.std', '.tail', '.to_csv', '.to_excel', 
             '.to_json', '.to_sql', '.value_counts', 'df', 'iloc', 'loc'
            ]
        }
