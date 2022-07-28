# Initiate dcitionary of lists with syntax sets. Default is syntax

list_ = {
        #Common Syntax Characters - Default
        
        "syntax": 

            [ "*","(",")","_","+",
            "{","}","|","[","]","\\",
            ":",'"',"'",";","'",
            "<",">","?",",",".","?",
            "%","#","!","~","`","^","&" 
            ],

        #Common git Commands          
        #   
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
            ],

        # Common SQL functionality

        "sql" : 

            ['(*)',');',',',';','ADD COLUMN','ALL','ALTER TABLE','AND','AVG()','BETWEEN','BIGINT','BOOLEAN',
            'CASCADE','COUNT()','CROSS JOIN','DEFAULT','DELETE FROM','DESC','DROP TABLE IF EXISTS',
            'EXISTS','FROM','FULL JOIN','FULL OUTER JOIN','GROUP BY','HAVING','IN','INNER JOIN','INSERT INTO',
            'INTO','IS NOT NULL','JOIN','LEFT JOIN','LIKE','MAX()','MIN()','NATURAL JOIN','NULL','ON','OR','ORDER BY',
            'PRIMARY KEY','REMOVE','RIGHT JOIN','SELECT','SUM()','TRUE','WHERE','[ASC]','_%'
            ]
                # Query order of execution

                        # 1. FROM and JOINs

                # The FROM clause, and subsequent JOINs are first executed to determine the 
                # total working set of data that is being queried. This includes subqueries in
                # this clause, and can cause temporary tables to be created under the hood 
                # containing all the columns and rows of the tables being joined.

                        # 2. WHERE

                # Once we have the total working set of data, the first-pass WHERE constraints 
                # are applied to the individual rows, and rows that do not satisfy the constraint 
                # are discarded. Each of the constraints can only access columns directly from the 
                # tables requested in the FROM clause. Aliases in the SELECT part of the query are 
                # not accessible in most databases since they may include expressions dependent on
                # parts of the query that have not yet executed.

                        # 3. GROUP BY

                # The remaining rows after the WHERE constraints are applied are then grouped 
                # based on common values in the column specified in the GROUP BY clause. 
                # As a result of the grouping, there will only be as many rows as there are unique 
                # values in that column. Implicitly, this means that you should only need to use this 
                # when you have aggregate functions in your query.

                        # 4. HAVING

                # If the query has a GROUP BY clause, then the constraints in the HAVING 
                # clause are then applied to the grouped rows, discard the grouped rows 
                # that don't satisfy the constraint. Like the WHERE clause, aliases are also 
                # not accessible from this step in most databases.

                        # 5. SELECT

                # Any expressions in the SELECT part of the query are finally computed.

                        # 6. DISTINCT

                # Of the remaining rows, rows with duplicate values in the column marked as DISTINCT will be discarded.

                        # 7. ORDER BY

                # If an order is specified by the ORDER BY clause, the rows are then sorted by the specified
                #  data in either ascending or descending order. Since all the expressions in the SELECT
                #   part of the query have been computed, you can reference aliases in this clause.

                        # 8. LIMIT / OFFSET

                # Finally, the rows that fall outside the range specified by the LIMIT and OFFSET are
                #  discarded, leaving the final set of rows to be returned from the query.

                # Conclusion

                # Not every query needs to have all the parts we listed above, but a part of why SQL
                #  is so flexible is that it allows developers and data analysts to quickly manipulate
                #   data without having to write additional code, all just by using the above clauses.

                    #Complete SELECT query

                    # SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
                    # FROM mytable
                    #     JOIN another_table
                    #     ON mytable.column = another_table.column
                    #     WHERE constraint_expression
                    #     GROUP BY column
                    #     HAVING constraint_expression
                    #     ORDER BY column ASC/DESC
                    #     LIMIT count OFFSET COUNT;
        
       
       
        }