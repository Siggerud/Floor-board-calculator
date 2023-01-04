from tkinter import Label, Entry, Button, IntVar, Tk, Text, END
from floorLayingCalculator import FloorLayingCalculator
from PIL import Image, ImageTk

class floorLayingGUI:
	def __init__(self, master):
		"""GUI for calculating material need for floor laying"""
		self.master = master
		master.title("Floor board calculator")
		master.geometry("550x450")
		
		font_tuple = ("Arial", 10, "bold")
		pady=2

		inputLabel = Label(master, text="Floor dimensions in mm", font=("Arial", 12, "bold"))
		inputLabel.grid(row=0, column=1, sticky="w", pady=5, columnspan=2)

		roomGeometryLabel1 = Label(master, text="A (parallel to boards)", font = font_tuple)
		roomGeometryLabel1.grid(row=1, column=0, sticky="w", pady=pady)
		
		self.length = IntVar()
		self.length.set(5000)
		roomGeometryEntry1 = Entry(master, textvariable=self.length)
		roomGeometryEntry1.grid(row=1, column=1, padx=10)
		
		roomGeometryLabel2 = Label(master, text="B", font = font_tuple)
		roomGeometryLabel2.grid(row=2, column=0, sticky="w", pady=pady)
		
		self.width = IntVar()
		self.width.set(4000)
		roomGeometryEntry2 = Entry(master, textvariable=self.width)
		roomGeometryEntry2.grid(row=2, column=1)
		
		lengthPerBoardLabel = Label(master, text="Board length", font = font_tuple)
		lengthPerBoardLabel.grid(row=3, column=0, sticky="w", pady=pady)
		
		self.boardLength = IntVar()
		self.boardLength.set(3000)
		lengthPerBoardEntry = Entry(master, textvariable=self.boardLength)
		lengthPerBoardEntry.grid(row=3, column=1)
		
		widthPerBoardLabel = Label(master, text = "Board width", font = font_tuple)
		widthPerBoardLabel.grid(row=4, column=0, sticky="w", pady=pady)
		
		self.boardWidth = IntVar()
		self.boardWidth.set(270)
		widthPerBoardEntry = Entry(master, textvariable=self.boardWidth)
		widthPerBoardEntry.grid(row=4, column=1)
		
		minimumBoardLengthLabel = Label(master, text="Minimum board length", font=font_tuple)
		minimumBoardLengthLabel.grid(row=5, column=0, sticky="w", pady=pady)
		
		self.minimumBoardLength = IntVar()
		self.minimumBoardLength.set(300)
		minimumBoardLengthEntry = Entry(master, textvariable=self.minimumBoardLength)
		minimumBoardLengthEntry.grid(row=5, column=1)

		minimumBoardWidthLabel = Label(master, text="Minimum board width", font=font_tuple)
		minimumBoardWidthLabel.grid(row=6, column=0, sticky="w", pady=pady)

		self.minimumBoardWidth = IntVar()
		self.minimumBoardWidth.set(50)
		minimumBoardWidthEntry = Entry(master, textvariable=self.minimumBoardWidth)
		minimumBoardWidthEntry.grid(row=6, column=1)

		gapLabel = Label(master, text="Gap", font=font_tuple)
		gapLabel.grid(row=7, column=0, sticky="w", pady=pady)

		self.gap = IntVar()
		self.gap.set(15)
		gapEntry = Entry(master, textvariable=self.gap)
		gapEntry.grid(row=7, column=1)
        
		calcButton = Button(master, text="Calculate", command=self.getcalculations)
		calcButton.grid(row=8, column=1)

		# inserting image
		floorBoardImage = Image.open("floorBoards.png")
		floorBoardImage = floorBoardImage.resize((200, 200))
		floorBoardImageTk = ImageTk.PhotoImage(floorBoardImage)

		floorBoardImageLabel = Label(image=floorBoardImageTk)
		floorBoardImageLabel.image =floorBoardImageTk
		floorBoardImageLabel.grid(row=1, column=3, rowspan=7)

	def addOutputTextWidget(self, boardCount, boardLengthUsed, boardLengthTotal, usedArea, totalArea, discardArea, discardLength):
		"""Adds all output text in a new widget"""
		outPutText = Text(self.master, width=30, height=10)
		outPutText.grid(row=9, column=0, columnspan=2)

		text = f"""Number of boards: {boardCount}
		
Total board length: {boardLengthTotal} m
Used board length: {boardLengthUsed} m
Discard Length: {discardLength} m

Total area: {totalArea:.2f} m^2
Used area: {usedArea:.2f} m^2
Discard area: {discardArea:.2f} m^2
"""
		outPutText.insert(END, text)
        
	def getcalculations(self):
		"""Retrieves output data from the floorLayingCalculator object"""
		length = self.length.get()
		width = self.width.get()
		boardLength = self.boardLength.get()
		boardWidth = self.boardWidth.get()
		minumumBoardLength = self.minimumBoardLength.get()
		minimumBoardWidth = self.minimumBoardWidth.get()
		gap = self.gap.get()

		floorCalc = FloorLayingCalculator(length, width, boardLength, boardWidth, minumumBoardLength, minimumBoardWidth, gap)
		boardCount = floorCalc.boardCount
		boardLengthUsed = floorCalc.boardLengthUsed
		boardLengthTotal = floorCalc.boardLengthTotal
		usedArea = floorCalc.usedArea
		totalArea = floorCalc.totalArea
		discardArea = floorCalc.discardArea
		discardLength = floorCalc.discardLength

		self.addOutputTextWidget(boardCount, boardLengthUsed, boardLengthTotal, usedArea, totalArea, discardArea, discardLength)


master = Tk()
myGUI = floorLayingGUI(master)
master.mainloop()