{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "91f6f3d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "49761f92",
   "metadata": {},
   "outputs": [],
   "source": [
    "cap = cv2.VideoCapture(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "00d4721c",
   "metadata": {},
   "outputs": [],
   "source": [
    "status, photo=cap.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "9eadde1b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cv2.imwrite('myphoto.png',photo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "ee9acc46",
   "metadata": {},
   "outputs": [],
   "source": [
    "cap.release()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "940aa6c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "cv2.imshow('myimage',photo)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
