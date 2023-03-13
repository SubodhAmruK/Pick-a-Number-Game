"""
mw -> MainLoop -> Code is written inside it

w [1,2,3] -> Functions -> w1() -> Code for Main Page -> first called without any action
                              w2() -> Code for Second Page/Mode Options -> Called when Play button is clicked on Main Page
                                 w3() -> Code for Third Page/Easy Mode -> Called when Easy Button is clicked on Second Page

d[1,2] -> Functions ->  d1() -> destroys w2() and calls w1() -> Given for Back Buttons
                              d2() -> destroys w3() and calls w2() -> Given for Back Buttons

manage() -> Has the code which has the BackEnd for EasyMode

t [1-4] -> Labels       -> Used for Titles
p [1-7] -> Buttons      -> Used for Buttons
b [1-6] -> Buttons      -> Used for Buttons
l [1-30] -> Labels       -> used for Headings

e [1- 5] -> Entry Boxes  -> used for Number inputs
f [1-8] -> Frames       -> Used for storing labels,buttons,entries

w1() -> f1,f11,f12,t1,p[1,6] -> Main Page
w2() -> f2,t2,p[2,3,4,5] -> Second Page
w3() -> f[3,4,5,6],e1,l[1,2,3,4,5,6,7,8,9] -> Easy Mode [Third Page]

f1 = First/Main Page -> t1,p1,p6
f2 = Second/Mode Page -> t2,p3,p4,p5,p6
f3 = Third/EasyMode [Choice Checker] -> l2,l3,l4,l5
f4 = Third/EasyMode [Entry Box and Text] -> e1,l1
f5 = Third/EasyMode [Control Buttons - Play, Back, Exit] -> b1,b2,b3
f6 = Third/EasyMode [Score Counter] -> l6,l7,l8,l9

"""
from tkinter import *
from random import *

# from tkinter import messagebox

mw = Tk()
'''
mw.geometry("700x350")
bg = PhotoImage(file="bgi1.png")
bgi = Label(mw,image=bg)
bgi.place(x=0,y=0)
'''
mw.iconbitmap("Resources//Team.png")
exb = PhotoImage(file="Resources//exit.png")
maintit = PhotoImage(file="Resources//maintit.png")
tit1 = PhotoImage(file="Resources//Title_1.png")
tit2 = PhotoImage(file="Resources//Title_21.png")
play = PhotoImage(file="Resources//play.png")
easy = PhotoImage(file="Resources//easy.png")
medium = PhotoImage(file="Resources//medium.png")
hard = PhotoImage(file="Resources//hard.png")
Back = PhotoImage(file="Resources//Back.png")
info = PhotoImage(file="Resources//info.png")
team = PhotoImage(file="Resources//Team.png")

reset = PhotoImage(file="Resources//reset.png")
comp = PhotoImage(file="Resources//computer.png")
player = PhotoImage(file="Resources//player.png")
score = PhotoImage(file="Resources//score.png")
rounds = PhotoImage(file="Resources//round.png")
welcome = PhotoImage(file="Resources//welcome.png")
win = PhotoImage(file="Resources//win.png")
lost = PhotoImage(file="Resources//loose.png")
nument0_6 = PhotoImage(file="Resources//numentry.png")
nument0_1 = PhotoImage(file="Resources//numentry01.png")
nument0_9 = PhotoImage(file="Resources//numentry09.png")
choose0_1 = PhotoImage(file="Resources//choose01.png")
choose0_6 = PhotoImage(file="Resources//choose06.png")
choose0_9 = PhotoImage(file="Resources//choose09.png")
count = PhotoImage(file="Resources//counter.png")
info_pg = PhotoImage(file="Resources//infopg.png")
e_mode = PhotoImage(file="Resources//easymode.png")
m_mode = PhotoImage(file="Resources//medimode.png")
h_mode = PhotoImage(file="Resources//hardmode.png")
strp = PhotoImage(file="Resources//strp.png")
strp2 = PhotoImage(file="Resources//strp2.png")
e_instruct = PhotoImage(file="Resources//e_instruct.png")
m_instruct = PhotoImage(file="Resources//m_instruct.png")
h_instruct = PhotoImage(file="Resources//h_instruct.png")
exmsg = PhotoImage(file="Resources//ex_msg.png")
yes = PhotoImage(file="Resources//yes.png")
no = PhotoImage(file="Resources//no.png")
save = PhotoImage(file="Resources//save.png")

text_font = ("Impact", 25)
title_font = ("Impact", 50)
x_cord = 450
y_cord = 200
bgr = '#cd2f50'
bgw = 'WHITE'
bgb = 'BLACK'


def w1():
    def inpg():
        def d4():
            w1()
            inp.destroy()
            t3.destroy()

        t3.destroy()
        i.destroy()
        tm.destroy()
        p1.destroy()
        p6.destroy()
        inp = Label(mw, image=info_pg, bg=bgr, highlightthickness=0, relief="flat")
        stp = Label(mw, image=strp, bg=bgr, highlightthickness=0, relief="flat")
        p7 = Button(mw, image=Back, command=d4, bg=bgr, highlightthickness=0, relief="flat")  # Back Button

        p7.pack()
        p7.place(x=20, y=20)
        inp.pack()
        inp.place(x=-30, y=120)
        stp.pack()
        stp.place(x=1400, y=0)

    def w2():
        def d1():
            f2.destroy()  # destroys Mode/second page
            p5.destroy()
            t3.destroy()
            t4.destroy()
            w1()

        # Mode Options FrondEnd starts
        i.destroy()  # destroys main/fist page
        p1.destroy()  # destroys main/fist page
        f2 = LabelFrame(mw, padx=10, pady=10, bg=bgb, highlightthickness=0,
                        borderwidth=0)  # creates a frame that has Modes[easy, medium hard]
        f2.pack()
        f2.place(x=300, y=600)

        t2 = Label(f2, image=tit2, bg=bgw)

        # Mode Options FrondEnd temp-end
        # **************************************************************************
        # Easy Mode Starts
        def w4():

            def d3():
                f7.destroy()
                f8.destroy()
                b4.destroy()
                t1.destroy()
                # b9.destroy()
                # t3.destroy()
                w2()

            p5.config(command=d3)
            f2.destroy()  # destroys pick a mode page
            t3.destroy()
            t4.destroy()

            # Easy Mode BackEnd Starts
            def man2():  # Easy Mode BackEnd
                global i2  # Round Incrementer
                global s2  # Score Incrementer

                r = e2.get()

                if r != "":
                    if '0' <= r <= '1' and 0 <= int(r) <= 1:
                        q = randint(0, 1)  # inputs random integer b/w 0 to 1
                        l14.config(text=q, font=text_font)
                        i2 += 1
                        if i2 <= 9:
                            l17.config(text='0' + str(i2), font=text_font)
                        else:
                            l17.config(text=i2, font=text_font)

                        p = int(r)
                        if p == q:
                            s2 += 1
                            l11.config(image=win)
                            l15.config(text=p, font=text_font)
                            if s2 <= 9:
                                l18.config(text='0' + str(s2), font=text_font)
                            else:
                                l18.config(text=s2, font=text_font)
                            e2.delete(0, END)
                        else:
                            l11.config(image=lost)
                            l15.config(text=p, font=text_font)
                            e2.delete(0, END)
                    else:
                        l11.config(image=choose0_1)
                        l14.config(text=' - ', font=text_font)
                        l15.config(text=' - ', font=text_font)
                        e2.delete(0, END)
                else:
                    l11.config(image=nument0_1)
                    l14.config(text=' - ', font=text_font)
                    l15.config(text=' - ', font=text_font)
                    e2.delete(0, END)

            def man4():
                global i2  # Round Incrementer
                global s2  # Score Incrementer
                i2 = 1
                s2 = 0
                l11.config(image=nument0_1)
                l17.config(text='01', font=text_font)
                l18.config(text='00', font=text_font)
                l14.config(text=' - ', font=text_font)
                l15.config(text=' - ', font=text_font)

                e2.delete(0, END)

            '''def r1():
                # global i2  # Round Incrementer
                if int(i2 - 1) == 0:
                    pass
                else:
                    f = open('datafile.txt', "a")
                    f.write("Mode: Easy  ")
                    f.write("      Rounds played: ")
                    f.write(str(i2 - 1))
                    f.write("      Score: ")
                    f.write(str(s2))
                    f.write("\n")
                    f.close()

                f = open("datafile.txt", "r")
                print(f.read())'''

            # Easy Mode BackEnd Ends
            # Easy Mode FrondEnd Starts
            t1 = Label(mw, image=tit1, bg=bgr)
            t1.pack()
            t1.place(x=330, y=20)

            f7 = LabelFrame(mw, padx=10, pady=10, bg=bgr, highlightthickness=0, borderwidth=0)  # ThirdPage
            f7.pack(padx=10, pady=10)
            f7.place(x=20, y=y_cord - 15)

            f8 = LabelFrame(mw, padx=10, pady=10, bg='#000000', highlightthickness=0, borderwidth=0)  # ThirdPage
            f8.pack(padx=10, pady=10)
            f8.place(x=x_cord - 100, y=y_cord)

            l20 = Label(f8, image=welcome, bg=bgw)  # Hello Box
            e2 = Entry(f8, width=45, font=text_font, justify='center')  # Entry Box
            l11 = Label(f8, image=nument0_1, bg=bgw)  # Number title

            l16 = Label(f8, image=rounds, bg=bgb)
            l17 = Label(f8, text='01', font=text_font, bg=bgw, fg="BLACK", pady=21, padx=21)  # round
            l19 = Label(f8, image=score, bg=bgb)
            l18 = Label(f8, text='00', font=text_font, bg=bgw, fg="BLACK", pady=21, padx=21)  # score
            b4 = Button(f8, image=play, command=man2, highlightthickness=0, relief="flat")  # Play Button
            b5 = Button(f8, image=reset, command=man4, highlightthickness=0, relief="flat")  # Reset Button
            # b9 = Button(mw, image=save, command=r1, highlightthickness=0, bg=bgb, relief="flat")  # Save Button

            l26 = Label(f7, image=e_mode, bg=bgr)
            l28 = Label(f7, image=e_instruct, bg=bgr)

            l12 = Label(f8, image=comp, bg=bgb)
            l14 = Label(f8, text=' - ', font=text_font, bg=bgw, fg="BLACK", pady=21, padx=21)  # comp choice
            l13 = Label(f8, image=player, bg=bgb)
            l15 = Label(f8, text=' - ', font=text_font, bg=bgw, fg="BLACK", pady=21, padx=21)  # your_choice

            l26.grid(row=0, column=0, pady=3, columnspan=9)  # Mode Display
            l28.grid(row=1, column=0, pady=3, columnspan=9)  # Mode Instruct Display

            l20.grid(row=0, column=0, pady=20, columnspan=3)  # Hello Box

            l16.grid(row=1, column=0, pady=3)  # Shows Round
            l17.grid(row=1, column=0, pady=3, sticky=E)
            l19.grid(row=1, column=2, pady=3)  # Show Score
            l18.grid(row=1, column=2, pady=3, sticky=W)

            l12.grid(row=2, column=0, pady=3)  # Computer Choice
            l14.grid(row=2, column=0, pady=3, sticky=E)
            l13.grid(row=2, column=2, pady=3)  # Your Choice
            l15.grid(row=2, column=2, pady=3, sticky=W)

            e2.grid(row=3, column=0, pady=10, padx=30, columnspan=3)  # Entry Box
            l11.grid(row=4, column=0, pady=10, columnspan=3)  # Enter Instruction

            b4.grid(row=5, column=0, pady=10, sticky=W)  # Play Button attributes
            b5.grid(row=5, column=2, pady=10, sticky=E)  # Reset Button attributes
            '''b9.pack()  # Save Button attributes
            b9.place(x=665, y=693)'''

        # Easy Mode FrondEnd Ends
        # **************************************************************************************************
        # Medium Mode Starts
        def w3():
            def d2():
                t1.destroy()
                f3.destroy()
                f4.destroy()
                b1.destroy()
                # b9.destroy()
                # t3.destroy()
                w2()

            t3.destroy()
            t4.destroy()
            f2.destroy()  # destroys pick a mode page
            p5.config(command=d2)

            # Medium Mode BackEnd Starts
            def man1():  # Medium Mode BackEnd
                global i1  # Round Incrementer
                global s1  # Score Incrementer
                r = e1.get()
                if r != "":
                    if '1' <= r <= '6' and 1 <= int(r) <= 6:
                        q = randint(1, 6)  # inputs random integer b/w 0 to 6
                        l4.config(text=q, font=text_font)
                        i1 += 1
                        if i1 <= 9:
                            l7.config(text='0' + str(i1), font=text_font)
                        else:
                            l7.config(text=i1, font=text_font)
                        p = int(r)
                        if p == q:
                            s1 += 1
                            l1.config(image=win)
                            l5.config(text=p, font=text_font)
                            if s1 <= 9:
                                l8.config(text='0' + str(s1), font=text_font)
                            else:
                                l8.config(text=s1, font=text_font)
                            e1.delete(0, END)
                        else:
                            l1.config(image=lost)
                            l5.config(text=p, font=text_font)
                            e1.delete(0, END)
                    else:
                        l1.config(image=choose0_6)
                        l4.config(text=' - ', font=text_font)
                        l5.config(text=' - ', font=text_font)
                        e1.delete(0, END)
                else:
                    l1.config(image=nument0_6)
                    l4.config(text=' - ', font=text_font)
                    l5.config(text=' - ', font=text_font)
                    e1.delete(0, END)

            '''def r1():
                # global i2  # Round Incrementer
                if int(i1 - 1) == 0:
                    pass
                else:
                    f = open('datafile.txt', "a")
                    f.write("Mode: Medium")
                    f.write("      Rounds played: ")
                    f.write(str(i1 - 1))
                    f.write("      Score: ")
                    f.write(str(s1))
                    f.write("\n")
                    f.close()

                f = open("datafile.txt", "r")
                print(f.read())'''

            def man3():
                global i1  # Round Incrementer
                global s1  # Score Incrementer
                i1 = 1
                s1 = 0
                l1.config(image=nument0_6)
                l4.config(text=' - ', font=text_font)
                l7.config(text='01', font=text_font)
                l5.config(text=' - ', font=text_font)
                l8.config(text='00', font=text_font)
                e1.delete(0, END)

            # Medium Mode BackEnd Ends
            # Medium Mode FrondEnd Starts
            t1 = Label(mw, image=tit1, bg=bgr)
            t1.pack()
            t1.place(x=330, y=20)

            f3 = LabelFrame(mw, padx=10, pady=10, bg=bgr, highlightthickness=0, borderwidth=0)  # ThirdPage
            f3.pack(padx=10, pady=10)
            f3.place(x=20, y=y_cord - 15)

            f4 = LabelFrame(mw, padx=10, pady=10, bg='#000000', highlightthickness=0, borderwidth=0)  # ThirdPage
            f4.pack(padx=10, pady=10)
            f4.place(x=x_cord - 100, y=y_cord)

            l10 = Label(f4, image=welcome, bg=bgw)  # Hello Box
            e1 = Entry(f4, width=45, font=text_font, justify='center')  # Entry Box
            l1 = Label(f4, image=nument0_6, bg=bgw)  # Number title

            l6 = Label(f4, image=rounds, bg=bgb)
            l7 = Label(f4, text='01', font=text_font, bg=bgw, fg="BLACK", pady=21, padx=21)  # round
            l9 = Label(f4, image=score, bg=bgb)
            l8 = Label(f4, text='00', font=text_font, bg=bgw, fg="BLACK", pady=21, padx=21)  # score

            b1 = Button(f4, image=play, command=man1, highlightthickness=0, relief="flat")  # Play Button
            b6 = Button(f4, image=reset, command=man3, highlightthickness=0, relief="flat")  # Reset Button
            # b9 = Button(mw, image=save, command=r1, highlightthickness=0, bg=bgb, relief="flat")  # Save Button

            l27 = Label(f3, image=m_mode, bg=bgr)
            l29 = Label(f3, image=m_instruct, bg=bgr)

            l2 = Label(f4, image=comp, bg=bgb)
            l4 = Label(f4, text=' - ', font=text_font, bg=bgw, fg="BLACK", pady=21, padx=21)  # comp choice
            l3 = Label(f4, image=player, bg=bgb)
            l5 = Label(f4, text=' - ', font=text_font, bg=bgw, fg="BLACK", pady=21, padx=21)  # your_choice

            l10.grid(row=0, column=0, pady=10, columnspan=3)  # Hello Box

            l6.grid(row=1, column=0, pady=3)  # Shows Round
            l7.grid(row=1, column=0, pady=3, sticky=E)
            l9.grid(row=1, column=2, pady=3)  # Show Score
            l8.grid(row=1, column=2, pady=3, sticky=W)

            l2.grid(row=2, column=0, pady=3)  # Computer Choice
            l4.grid(row=2, column=0, pady=3, sticky=E)
            l3.grid(row=2, column=2, pady=3)  # Your Choice
            l5.grid(row=2, column=2, pady=3, sticky=W)

            e1.grid(row=3, column=0, pady=10, padx=30, columnspan=3)  # Entry Box
            l1.grid(row=4, column=0, pady=10, columnspan=3)  # Enter Instruction

            b1.grid(row=5, column=0, pady=10, sticky=W)  # Play Button attributes
            b6.grid(row=5, column=2, pady=10, sticky=E)  # Reset Button attributes
            '''b9.pack()  # Save Button attributes
            b9.place(x=650, y=673)'''

            l27.grid(row=0, column=0, pady=3, columnspan=9)  # Mode Display
            l29.grid(row=1, column=0, pady=3, columnspan=9)  # Mode Instruct Display

        # Medium Mode FrondEnd Ends
        # ***************************************************************************************
        # Hard Mode Starts
        def w5():
            def d5():
                # t3.destroy()
                t1.destroy()
                f11.destroy()
                f12.destroy()
                b4.destroy()
                # b9.destroy()
                w2()

            p5.config(command=d5)
            t3.destroy()
            t4.destroy()
            f2.destroy()  # destroys pick a mode page

            # Hard Mode BackEnd Starts
            def man5():  # Hard Mode BackEnd

                global s3  # Score Incrementer
                a = e3.get()
                b = e4.get()
                c = e5.get()

                if a != "" and b != "" and c != "":
                    if '0' <= a <= '9' and '0' <= b <= '9' and '0' <= c <= '9' and 0 <= int(a) <= 9 and 0 <= int(
                            b) <= 9 and 0 <= int(c) <= 9:
                        q1 = randint(0, 3)  # inputs random integer b/w 0 to 9
                        q2 = randint(4, 6)  # inputs random integer b/w 0 to 9
                        q3 = randint(7, 9)  # inputs random integer b/w 0 to 9

                        '''q1 = 0
                        q2 = 4
                        q3 = 7'''

                        l14.config(text=q1, font=text_font)
                        l21.config(text=q2, font=text_font)
                        l22.config(text=q3, font=text_font)

                        pp1 = int(a)
                        pp2 = int(b)
                        pp3 = int(c)

                        global i3  # Round Incrementer
                        i3 += 1
                        if i3 <= 9:
                            l17.config(text='0' + str(i3), font=text_font)
                        else:
                            l17.config(text=i3, font=text_font)
                        if pp1 == q1 and pp2 == q2 and pp3 == q3:
                            s3 += 3
                            l11.config(image=win)
                            l15.config(text=pp1, font=text_font)
                            l23.config(text=pp2, font=text_font)
                            l24.config(text=pp3, font=text_font)

                            if s3 <= 9:
                                l18.config(text='0' + str(s3), font=text_font)
                            else:
                                l18.config(text=s3, font=text_font)
                            e3.delete(0, END)
                            e4.delete(0, END)
                            e5.delete(0, END)
                        else:
                            l11.config(image=lost)
                            l15.config(text=pp1, font=text_font)
                            l23.config(text=pp2, font=text_font)
                            l24.config(text=pp3, font=text_font)
                            e3.delete(0, END)
                            e4.delete(0, END)
                            e5.delete(0, END)
                    else:
                        l11.config(image=choose0_9)
                        l14.config(text='-', font=text_font)
                        l21.config(text='-', font=text_font)
                        l22.config(text='-', font=text_font)
                        l15.config(text='-', font=text_font)
                        l23.config(text='-', font=text_font)
                        l24.config(text='-', font=text_font)
                        e3.delete(0, END)
                        e4.delete(0, END)
                        e5.delete(0, END)
                else:
                    l11.config(image=nument0_9)
                    l14.config(text='-', font=text_font)
                    l21.config(text='-', font=text_font)
                    l22.config(text='-', font=text_font)
                    l15.config(text='-', font=text_font)
                    l23.config(text='-', font=text_font)
                    l24.config(text='-', font=text_font)

                    e3.delete(0, END)
                    e4.delete(0, END)
                    e5.delete(0, END)

            '''def r1():
                # global i2  # Round Incrementer
                if int(i3 - 1) == 0:
                    pass
                else:
                    f = open('datafile.txt', "a")
                    f.write("Mode: Hard  ")
                    f.write("      Rounds played: ")
                    f.write(str(i3 - 1))
                    f.write("       Score: ")
                    f.write(str(s3))
                    f.write("\n")
                    f.close()

                f = open("datafile.txt", "r")
                print(f.read())'''

            def man4():
                global i3  # Round Incrementer
                global s3  # Score Incrementer
                i3 = 1
                s3 = 0
                l11.config(image=nument0_9)
                l17.config(text='01', font=text_font)
                l18.config(text='00', font=text_font)

                l14.config(text='-', font=text_font)
                l21.config(text='-', font=text_font)
                l22.config(text='-', font=text_font)

                l15.config(text='-', font=text_font)
                l23.config(text='-', font=text_font)
                l24.config(text='-', font=text_font)

                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

            # Hard Mode BackEnd Ends
            # Hard Mode FrondEnd Starts
            t1 = Label(mw, image=tit1, bg=bgr)
            t1.pack()
            t1.place(x=330, y=20)

            f11 = LabelFrame(mw, padx=10, pady=10, bg=bgr, highlightthickness=0, borderwidth=0)  # ThirdPage
            f11.pack(padx=10, pady=10)
            f11.place(x=20, y=y_cord - 55)

            f12 = LabelFrame(mw, padx=10, pady=10, bg='#000000', highlightthickness=0, borderwidth=0)  # ThirdPage
            f12.pack(padx=10, pady=10)
            f12.place(x=x_cord - 100, y=y_cord - 40)

            l25 = Label(f11, image=h_mode, bg=bgr)  # Mode Display
            l30 = Label(f11, image=h_instruct, bg=bgr)  # Mode instruct Display

            l20 = Label(f12, image=welcome, bg=bgw)  # Hello Box

            l16 = Label(f12, image=rounds, bg=bgb)
            l17 = Label(f12, text='01', font=text_font, bg=bgw, fg="BLACK", pady=21, padx=21)  # round
            l19 = Label(f12, image=score, bg=bgb)
            l18 = Label(f12, text='00', font=text_font, bg=bgw, fg="BLACK", pady=21, padx=21)  # score

            l12 = Label(f12, image=comp, bg='#000000')
            l14 = Label(f12, text='-', font=text_font, bg=bgb, fg="WHITE", pady=21, padx=30)  # comp choice 1
            l21 = Label(f12, text='-', font=text_font, bg=bgb, fg="WHITE", pady=21, padx=30)  # comp choice 2
            l22 = Label(f12, text='-', font=text_font, bg=bgb, fg="WHITE", pady=21, padx=30)  # comp choice 3

            l13 = Label(f12, image=player, bg='#000000')
            l15 = Label(f12, text=' - ', font=text_font, bg=bgb, fg="WHITE", pady=21, padx=30)  # your_choice 1
            l23 = Label(f12, text=' - ', font=text_font, bg=bgb, fg="WHITE", pady=21, padx=30)  # your_choice 2
            l24 = Label(f12, text=' - ', font=text_font, bg=bgb, fg="WHITE", pady=21, padx=30)  # your_choice 3

            e3 = Entry(f12, width=15, font=text_font, justify='center')  # Entry Box 1
            e4 = Entry(f12, width=15, font=text_font, justify='center')  # Entry Box 2
            e5 = Entry(f12, width=15, font=text_font, justify='center')  # Entry Box 3

            l11 = Label(f12, image=nument0_9, bg=bgw)  # Number title
            b4 = Button(f12, image=play, command=man5, highlightthickness=0, relief="flat")  # Play Button
            b5 = Button(f12, image=reset, command=man4, highlightthickness=0, relief="flat")  # Reset Button
            # b9 = Button(mw, image=save, command=r1, highlightthickness=0, bg=bgb, relief="flat")  # Save Button

            l25.grid(row=0, column=0, pady=3, columnspan=9)  # Mode display
            l30.grid(row=1, column=0, pady=3, columnspan=9)  # Mode instruct display

            l20.grid(row=0, column=0, pady=10, columnspan=3)  # Hello Box

            l16.grid(row=1, column=0, pady=3)  # Shows Round
            l17.grid(row=1, column=1, pady=3, sticky=W)  # rounds display
            l19.grid(row=1, column=2, pady=3)  # Show Score
            l18.grid(row=1, column=1, pady=3, sticky=E)  # Score display

            l12.grid(row=2, column=0, pady=3)  # Computer Choice
            l14.grid(row=2, column=1, pady=3, sticky=W)  # Computer Choice display 1
            l21.grid(row=2, column=1, pady=3)  # Computer Choice display 2
            l22.grid(row=2, column=1, pady=3, sticky=E)  # Computer Choice display 3

            l13.grid(row=3, column=2, pady=3)  # Your Choice
            l15.grid(row=3, column=1, pady=3, sticky=W)  # Your Choice Display 1
            l23.grid(row=3, column=1, pady=3)  # Your Choice Display 2
            l24.grid(row=3, column=1, pady=3, sticky=E)  # Your Choice Display 3

            e3.grid(row=4, column=0, pady=10, padx=10)  # Entry Box 1
            e4.grid(row=4, column=1, pady=10, padx=10)  # Entry Box 2
            e5.grid(row=4, column=2, pady=10, padx=10)  # Entry Box 3

            l11.grid(row=5, column=0, pady=10, columnspan=3)  # Enter Instruction

            b4.grid(row=6, column=0, pady=10, sticky=W)  # Play Button attributes
            b5.grid(row=6, column=2, pady=10, sticky=E)  # Reset Button attributes
            '''b9.pack()  # Save Button attributes
            b9.place(x=665, y=727)'''

        # Hard Mode FrondEnd Ends
        # **************************************************************************

        # Mode Options FrondEnd continues
        # t1 = Label(mw, image=tit1, bg=bgr)

        p2 = Button(f2, image=easy, command=w4, bg=bgw, highlightthickness=0, relief="flat")  # Easy Button
        p3 = Button(f2, image=medium, command=w3, bg=bgw, highlightthickness=0, relief="flat")  # Medium Button
        p4 = Button(f2, image=hard, command=w5, bg=bgw, highlightthickness=0, relief="flat")  # Hard Button
        p5 = Button(mw, image=Back, command=d1, bg=bgr, highlightthickness=0, relief="flat")  # Back Button
        t4 = Label(mw, image=maintit, bg=bgr)

        t2.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        p2.grid(row=1, column=0, pady=3, padx=3)
        p3.grid(row=1, column=1, pady=3, padx=3)
        p4.grid(row=1, column=2, pady=3, padx=3)
        p5.pack()
        p5.place(x=20, y=20)

        t4.pack()
        t4.place(x=-10, y=180)

        # t1.pack()
        # t1.place(x=330, y=20)

        # Mode Options FrondEnd Ends

    # **************************************************************************
    # Main Page FrondEnd Starts
    def ex():
        """msg = messagebox.askquestion("WARNING!", "Are you sure you want to exit?")
        if msg == 'yes':
            mw.destroy()
        else:
            pass"""

        f9 = LabelFrame(mw, padx=10, pady=5, bg=bgb, highlightthickness=0, borderwidth=0)  # ThirdPage
        f9.pack()
        f9.place(x=1000, y=15)

        l31 = Label(f9, image=exmsg, bg=bgw, highlightthickness=0, relief="flat")
        b7 = Button(f9, image=yes, command=mw.destroy, bg=bgw, highlightthickness=0, relief="flat",
                    borderwidth=0)
        b8 = Button(f9, image=no, command=f9.destroy, bg=bgb, highlightthickness=0, relief="flat",
                    borderwidth=0)

        l31.grid(row=0, column=0, columnspan=2, rowspan=2, pady=5)
        b7.grid(row=2, column=0, pady=5)
        b8.grid(row=2, column=1)

    t3 = Label(mw, image=maintit, bg=bgr)
    i = Button(mw, image=info, command=inpg, bg=bgr, highlightthickness=0, relief="flat")
    p1 = Button(mw, image=play, command=w2, highlightthickness=0, relief="flat")
    p6 = Button(mw, image=exb, command=ex, bg=bgr, highlightthickness=0, relief="flat")

    tm = Label(mw, image=team, bg=bgr)

    tm.pack()
    tm.place(x=1415, y=726)
    i.pack()
    i.place(x=20, y=35)
    t3.pack()
    t3.place(x=-10, y=180)
    p1.pack()
    p1.place(x=600, y=750)
    p6.pack()
    p6.place(x=1430, y=35)

    # Main Page FrondEnd Ends


i1, s1 = 1, 0
i2, s2 = 1, 0
i3, s3 = 1, 0

w1()  # calls the function
# mw.state('zoomed')
mw.attributes('-fullscreen', True)  # makes the game full screen
mw.configure(bg=bgr)  # Gives the background colour

mw.mainloop()
