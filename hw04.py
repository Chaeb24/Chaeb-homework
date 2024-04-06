def rep_char(c,n):
    print(c*n)

def draw_line_string(msg):
    nstr = len(msg1)if(len(msg1)>len(msg2))else len(msg2)
    rep_char('-',nstr)
    print(f'Hello {msg},')
    print('Welcome to Seoul.')
    rep_char('-',nstr)

msg1 = input('Input his/her name:')
msg2 = input('Input his/her name:')

draw_line_string(msg1)
draw_line_string(msg2)


            







    

