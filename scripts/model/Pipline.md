### 🧠 **Chessboard Recognition Pipeline**

#### **Stage 1: Screen to Cropped Board**

**Goal:** Detect and crop the chessboard from any screenshot of a chess game (Lichess, Chess.com, apps, etc.)

**Input:** Raw screenshot (RGB image)\
**Output:** Cropped, aligned chessboard image

**Options:** - 📦 **Option A: Classical CV (OpenCV)** - Convert to grayscale - Detect edges and find contours - Filter for square-ish, grid-like contour (8x8) - Warp/perspective transform the board

-   🤖 **Option B: ML-based Detection**
    -   Use a pre-trained object detection model (YOLOv5/8) fine-tuned on screenshots
    -   Predict bounding box → crop + warp to 8x8 square

------------------------------------------------------------------------

#### **Stage 2: Cropped Board to Board State**

**Goal:** Understand which piece is in which square

**Input:** Clean 8x8 board image (top-down)\
**Output:** FEN string or 8x8 matrix representing the board state

**Options:** - 🧩 **Option A: Square-wise Classifier** - Split into 64 squares (tiles) - For each tile → classify into 13 classes (empty, white/black × 6 pieces) - Use a CNN or lightweight ResNet for classification

-   🔤 **Option B: Full-board Image → FEN**
    -   Use a vision transformer (e.g., ViT) or CNN+LSTM model
    -   Predict full FEN string directly from image (harder to train, but elegant)

------------------------------------------------------------------------

#### **Stage 3: Board State to Suggested Move**

**Goal:** Use board state to predict or suggest a next move

**Input:** Board state (FEN)\
**Output:** Suggested best move (e.g., in UCI or SAN notation)

**Options:** - 🧠 Use a pre-trained chess engine (e.g., Stockfish via python-chess) - 🧠 Train your own move predictor (deep learning) \[optional/future\]

------------------------------------------------------------------------

### 🔁 Optional Enhancements

-   Multi-theme adaptation (train with different board/piece styles)
-   OCR or icon recognition to detect player names, move history
-   Time control and timer parsing
-   Drag-and-drop mouse automation to execute the move (if you plan to integrate into the trainer app)

------------------------------------------------------------------------


# Chess Trainer Detection Pipeline

## Stage 1: Screen Capture
- Capture the screen using mss or FFmpeg.
- Convert frame into proper format (BGR).

## Stage 2: Detection
- Use YOLOv11m model to detect chess pieces.
- Return bounding boxes, class IDs, and confidence scores.

## Stage 3: Overlay
- Pass detection data to the GUI overlay.
- Render bounding boxes over the screen using PySide6 overlay widget.

## Future
- Move prediction using engine (e.g., python-chess).
- Add real-time advice or hinting based on game state.
