class FloorLayingCalculator:
    def __init__(self, roomLength, roomWidth, boardLength, boardWidth, minimumBoardLength, minimumBoardWidth, gap):
        """Tool for calculating relevant material need metrics when laying a floor"""
        args = [roomLength, roomWidth, boardLength, boardWidth, minimumBoardLength, minimumBoardWidth, gap]

        for arg in args:
            if arg < 0:
                raise ValueError("Dimensions can't be negative")

        self.roomLength = roomLength
        self.roomWidth = roomWidth
        self.boardLength = boardLength
        self.boardWidth = boardWidth
        self.minimumBoardLength = minimumBoardLength
        self.minimumBoardWidth = minimumBoardWidth
        self.gap = gap
        self.boardCount = 0
        self.boardLengthUsed = 0
        self.boardLengthTotal = 0
        self.usedArea = 0
        self.totalArea = 0
        self.discardArea = 0
        self.discardLength = 0

        self.calculate()

    def calculate(self):
        """Calculates output values"""
        roomLength = self.roomLength
        roomWidth = self.roomWidth
        minimumBoardLength = self.minimumBoardLength
        minimumBoardWidth = self.minimumBoardWidth
        gap = self.gap

        realRoomLength = roomLength - 2*gap
        realRoomWidth = roomWidth - 2*gap

        self.calculateRestWidth(realRoomWidth)

        if self.restWidth < minimumBoardWidth:
            endWidths = self.getEndWidths()
        else:
            endWidths = self.boardWidth

        restBoard = 0
        boardCount = 0
        discardLength = 0
        workingWidth = 0
        while workingWidth < realRoomWidth:
            workingLength = 0
            while workingLength < realRoomLength:
                if workingWidth == 0 or workingWidth + endWidths - realRoomWidth < 1e-8:
                    boardWidth = endWidths
                else:
                    boardWidth = self.boardWidth

                if restBoard != 0:
                    boardLength = restBoard
                else:
                    boardLength = self.boardLength

                if workingLength + boardLength > realRoomLength:
                    if workingLength + boardLength - realRoomLength < minimumBoardLength:
                        discardLength += workingLength + boardLength - realRoomLength
                        restBoard = 0
                        boardCount += 1
                    else:
                        restBoard = workingLength + boardLength - realRoomLength
                    workingLength = realRoomLength
                    workingWidth += boardWidth

                else:
                    workingLength += boardLength
                    restBoard = 0
                    boardCount += 1

        if restBoard != 0:
            boardCount += 1
            discardLength += restBoard

        self.boardCount = boardCount
        self.boardLengthUsed = (boardCount * self.boardLength - discardLength) / 1000 # m
        self.boardLengthTotal = (boardCount * self.boardLength) / 1000
        self.usedArea = (realRoomLength * realRoomWidth) / 10**6 # m^2
        self.totalArea = (boardCount * self.boardWidth * self.boardLength) / 10**6 # m^2 endreeeeee
        self.discardArea = self.totalArea - self.usedArea # m^2 endreeeeeeeeee
        self.discardLength = discardLength / 1000 # m^2

    def getEndWidths(self):
        """Retrieves widths of first and last row of boards"""
        boardWidth = self.boardWidth
        restwidth = self.restWidth

        endWidth = (boardWidth + restwidth) / 2

        return endWidth

    def calculateRestWidth(self, realWidth):
        """Calculates width of last row of boards"""
        boardWidth = self.boardWidth

        self.restWidth = realWidth % boardWidth


