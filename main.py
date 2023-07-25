from tkinter import * 
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib import pyplot as plt, animation
from bubblesort import bubblesort
from insertionsort import insertionsort
from mergesort import mergesort
from countingsort import count_sort
from radixsort import radixSort
from quicksort import quicksort
from heapsort import heapSort
from bucketsort import bucketSort
from BookAlgo1 import hybrid_quick_sort
from BookAlgo2 import adv_countsort
from buildfiles import fillFile, readFile
from tkinter import filedialog as fd

N = int()
fileNo = 4
fileSizes = [10,50,100,1000]

for i in range(fileNo):
	fillFile(fileSizes[i],"file"+ str(i))

# helper methods
def swap(A, i, j):
	A[i], A[j] = A[j], A[i]


# def colorbar(A, color):
#     Canvas.delete("all")
#     Canvas_width=1250
#     Canvas_height=600
#     x_width=Canvas_width/(len(A) + 1)
#     offset = 4
#     spacing =2
#     normalizedData=[i/max(A) for i in A]

#     for i, height in enumerate(normalizedData):
#         x0=i*x_width+offset+spacing
#         y0=Canvas_height - height * 390
#         x1 =(i+1) * x_width + offset
#         y1=Canvas_height
#         Canvas.create_rectangle(x0,y0,x1,y1,fill=color[i])

#     window.update_idletasks()


# plot function is created for 
# plotting the graph in 
# tkinter window
def plot(): 
  
    # the figure that will contain the plot
    
    
    # creates a generator object containing all
    # the states of the array while performing
    # sorting algorithm
    generator = insertionsort(A)
    
    # creates a figure and subsequent subplots
    fig, ax = plt.subplots()
    fig.set_figwidth(25)
    fig.set_figheight(13)
    ax.set_title("Insertion Sort O(n\N{SUPERSCRIPT TWO})")
    bar_sub = ax.bar(range(N), A, align="edge", edgecolor = 'black', color='#ccccff')
    
    # sets the maximum limit for the x-axis
    ax.set_xlim(0, N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    
    # helper function to update each frame in plot
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")
        

    # creating animation object for rendering the iteration
    anim = animation.FuncAnimation(
        fig,
        func=update,
        fargs=(bar_sub, iteration),
        frames=generator,
        repeat=True,
        blit=False,
        interval=70,  #speed
        save_count=100,
    )
    
    # for showing the animation on screen
    #plt.show()
    
    #fig.subplots_adjust(left=0.05, bottom=0.07, right=0.95, top=0.95, wspace=2, hspace=5)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

def plot2():
    generator = bubblesort(A)
    
    # creates a figure and subsequent subplots
    fig2, ax = plt.subplots()
    fig2.set_figwidth(25)
    fig2.set_figheight(13)
    ax.set_title("Bubble Sort O(n)")
    bar_sub = ax.bar(range(len(A)), A, align="edge", edgecolor = 'black', color='#ccccff')
    ax.set_xlim(0, N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")
    anim = animation.FuncAnimation(fig2,func=update,fargs=(bar_sub, iteration),frames=generator,repeat=True,blit=False,interval=5,save_count=100,)
    canvas = FigureCanvasTkAgg(fig2, master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot3():
  
    # the figure that will contain the plot
    
    
    # creates a generator object containing all
    # the states of the array while performing
    # sorting algorithm
    generator = mergesort(A,0,2*N)
    
    # creates a figure and subsequent subplots
    fig3, ax = plt.subplots()
    fig3.set_figwidth(25)
    fig3.set_figheight(13)
    ax.set_title("Merge Sort O(n)")
    bar_sub = ax.bar(range(len(A)), A, align="edge", edgecolor = 'black', color='#ccccff')
    
    # sets the maximum limit for the x-axis
    ax.set_xlim(0, N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    
    # helper function to update each frame in plot
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")

    # creating animation object for rendering the iteration
    anim = animation.FuncAnimation(
        fig3,
        func=update,
        fargs=(bar_sub, iteration),
        frames=generator,
        repeat=True,
        blit=False,
        interval=110,
        save_count=90000,
    )
    
    # for showing the animation on screen
    #plt.show()
    
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig3, master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

def plot4():
    generator = count_sort(A, max(A))

    # creates a figure and subsequent subplots
    fig4, ax = plt.subplots()
    fig4.set_figwidth(25)
    fig4.set_figheight(13)
    ax.set_title("Count Sort O(n+k)")
    bar_sub = ax.bar(range(len(A)), A, align="edge", edgecolor = 'black', color='#ccccff')
    ax.set_xlim(0,N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")
    anim = animation.FuncAnimation(fig4,func=update,fargs=(bar_sub, iteration),frames=generator,repeat=True,blit=False,interval=5,save_count=100,)
    canvas = FigureCanvasTkAgg(fig4, master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot5():
    generator = heapSort(A)
    
    # creates a figure and subsequent subplots
    fig5, ax = plt.subplots()
    fig5.set_figwidth(25)
    fig5.set_figheight(13)
    ax.set_title("Heap Sort O(nlog(n))")
    bar_sub = ax.bar(range(len(A)), A, align="edge", edgecolor = 'black', color='#ccccff')
    ax.set_xlim(0, N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")
    anim = animation.FuncAnimation(fig5,func=update,fargs=(bar_sub, iteration),frames=generator,repeat=True,blit=False,interval=5,save_count=100,)
    canvas = FigureCanvasTkAgg(fig5, master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot6():
    generator = quicksort(A,0,N-1)
    
    # creates a figure and subsequent subplots
    fig6, ax = plt.subplots()
    fig6.set_figwidth(25)
    fig6.set_figheight(13)
    ax.set_title("Quick Sort O(nlog(n))")
    bar_sub = ax.bar(range(len(A)), A, align="edge", edgecolor = 'black', color='#ccccff')
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.1 * len(A)))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")
    anim = animation.FuncAnimation(fig6,func=update,fargs=(bar_sub, iteration),frames=generator,repeat=True,blit=False,interval=5,save_count=100,)
    canvas = FigureCanvasTkAgg(fig6, master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot7():
    generator = radixSort(A)
    
    # creates a figure and subsequent subplots
    fig7, ax = plt.subplots()
    fig7.set_figwidth(25)
    fig7.set_figheight(13)
    ax.set_title("Radix Sort O(nk)")
    bar_sub = ax.bar(range(len(A)), A, align="edge", edgecolor = 'black', color='#ccccff')
    ax.set_xlim(0, max(A))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")
    anim = animation.FuncAnimation(fig7,func=update,fargs=(bar_sub, iteration),frames=generator,repeat=True,blit=False,interval=5,save_count=100,)
    canvas = FigureCanvasTkAgg(fig7, master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot8():
    generator = bucketSort(A, 10)
    
    # creates a figure and subsequent subplots
    fig8, ax = plt.subplots()
    fig8.set_figwidth(25)
    fig8.set_figheight(13)
    ax.set_title("Bucket Sort O(n+k)")
    bar_sub = ax.bar(range(len(A)), A, align="edge", edgecolor = 'black', color='#ccccff')
    ax.set_xlim(0, len(A))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")
    anim = animation.FuncAnimation(fig8,func=update,fargs=(bar_sub, iteration),frames=generator,repeat=True,blit=False,interval=5,save_count=100,)
    canvas = FigureCanvasTkAgg(fig8, master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot9():
    generator = hybrid_quick_sort(A, 0, N-1)
    
    # creates a figure and subsequent subplots
    fig9, ax = plt.subplots()
    fig9.set_figwidth(25)
    fig9.set_figheight(13)
    ax.set_title("Algorithm 7.4-5 O(n\N{SUPERSCRIPT TWO})")
    bar_sub = ax.bar(range(len(A)), A, align="edge", edgecolor = 'black', color='#ccccff')
    ax.set_xlim(0, N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")
    anim = animation.FuncAnimation(fig9,func=update,fargs=(bar_sub, iteration),frames=generator,repeat=True,blit=False,interval=5,save_count=100,)
    canvas = FigureCanvasTkAgg(fig9, master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

def plot10():
    a=input("Enter lower bound value: ")
    b=input("Enter upper bound value: ")
    generator = adv_countsort(A, len(A), a,b)
    
    # creates a figure and subsequent subplots
    fig10, ax = plt.subplots()
    fig10.set_figwidth(25)
    fig10.set_figheight(13)
    ax.set_title("Algorithm 8.2-4 O(n\N{SUPERSCRIPT TWO})")
    bar_sub = ax.bar(range(len(A)), A, align="edge", edgecolor = 'black', color='#ccccff')
    ax.set_xlim(0, N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")
    anim = animation.FuncAnimation(fig10,func=update,fargs=(bar_sub, iteration),frames=generator,repeat=True,blit=False,interval=5,save_count=100,)
    canvas = FigureCanvasTkAgg(fig10, master = window)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()



# the main Tkinter window
window = Tk()
# setting the title 
window.title('Plotting in Tkinter')

frame = Frame(master=window, bg="#808080", relief=SUNKEN)
frame.pack(side=TOP, fill=X)
  
# dimensions of the main window
window.geometry("20000x4000")
algo_name = StringVar()
algorithms = [
    "Insertion sort",
    "Bubble sort",
    "Merge Sort",
    "Heap Sort",
    "Quick sort",
    "Radix Sort",
    "Bucket Sort"
]
file_name = StringVar()
files = [
    "File 1",
    "File 2",
    "File 3",
    "File 4"
]

filename = fd.askopenfilename()
print(filename)
if filename == 'C:/Users/warda/OneDrive/Desktop/test/file0.txt':
    N=10
elif filename == 'C:/Users/warda/OneDrive/Desktop/test/file1.txt':
    N=50
elif filename == 'C:/Users/warda/OneDrive/Desktop/test/file2.txt':
    N=100
else:
    N=1000

A=[int()]
A=readFile(filename)

# Create button

button1 = Button( master=frame , text = "Insertion Sort" , command = plot, relief=SUNKEN )
button1.grid(row=1,column=0,padx=10, ipadx=10,pady=10,ipady=10)

button2 = Button( master=frame , text = "Bubble Sort" , command = plot2, relief=SUNKEN )
button2.grid(row=1,column=1,padx=10, ipadx=10,pady=10,ipady=10)

button3 = Button( master=frame , text = "Merge Sort" , command = plot3, relief=SUNKEN )
button3.grid(row=1,column=2,padx=10, ipadx=10,pady=10,ipady=10)

button4 = Button( master=frame , text = "Counting Sort" , command = plot4, relief=SUNKEN )
button4.grid(row=1,column=3,padx=20, ipadx=10,pady=10,ipady=10)

button5 = Button( master=frame , text = "Heap Sort" , command = plot5, relief=SUNKEN )
button5.grid(row=1,column=4,padx=20, ipadx=10,pady=10,ipady=10)

button6 = Button( master=frame , text = "Quick Sort" , command = plot6, relief=SUNKEN )
button6.grid(row=1,column=5,padx=20, ipadx=10,pady=10,ipady=10)

button7 = Button( master=frame , text = "Radix Sort" , command = plot7, relief=SUNKEN )
button7.grid(row=1,column=6,padx=20, ipadx=10,pady=10,ipady=10)

button8 = Button( master=frame , text = "Bucket Sort" , command = plot8, relief=SUNKEN )
button8.grid(row=1,column=7,padx=20, ipadx=10,pady=10,ipady=10)

button9 = Button( master=frame , text = "Algorithm 7.4-5" , command = plot9, relief=SUNKEN)
button9.grid(row=1,column=8,padx=20, ipadx=10,pady=10,ipady=10)

button10 = Button( master=frame , text = "Algorithm 8.2-4" , command = plot10, relief=SUNKEN)
button10.grid(row=1,column=9,padx=20, ipadx=10,pady=10,ipady=10)


# run the gui
window.mainloop()
