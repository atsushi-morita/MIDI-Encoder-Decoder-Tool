import tkinter as tk
from tkinter import messagebox


def decode_midi():
    try:
        lsb = int(decode_lsb_entry.get(), 16)
        msb = int(decode_msb_entry.get(), 16)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid hexadecimal values.")
        return
    
    decoded_value = ((msb & 0x7F) << 7) | (lsb & 0x7F)
    decode_result_label.config(text=f"Decoded Value: {decoded_value}")


def encode_midi():
    try:
        value = int(encode_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer value.")
        return
    
    lsb = value & 0x7F
    msb = (value >> 7) & 0x7F
    encode_result_label.config(text=f"Encoded LSB: {hex(lsb)}  MSB: {hex(msb)}")


app = tk.Tk()
app.title("MIDI Encoder/Decoder")

# Decoder Frame
decode_frame = tk.Frame(app)
decode_frame.pack(padx=10, pady=10, fill='x')

tk.Label(decode_frame, text="MIDI Decoder", font='bold').grid(row=0, columnspan=2)
tk.Label(decode_frame, text="LSB (Hex):").grid(row=1, column=0)
decode_lsb_entry = tk.Entry(decode_frame)
decode_lsb_entry.grid(row=1, column=1)

tk.Label(decode_frame, text="MSB (Hex):").grid(row=2, column=0)
decode_msb_entry = tk.Entry(decode_frame)
decode_msb_entry.grid(row=2, column=1)

tk.Button(decode_frame, text="Decode", command=decode_midi).grid(row=3, columnspan=2, pady=10)
decode_result_label = tk.Label(decode_frame, text="Decoded Value: ")
decode_result_label.grid(row=4, columnspan=2)

# Encoder Frame
encode_frame = tk.Frame(app)
encode_frame.pack(padx=10, pady=10, fill='x')

tk.Label(encode_frame, text="MIDI Encoder", font='bold').grid(row=0, columnspan=2)
tk.Label(encode_frame, text="Value:").grid(row=1, column=0)
encode_entry = tk.Entry(encode_frame)
encode_entry.grid(row=1, column=1)

tk.Button(encode_frame, text="Encode", command=encode_midi).grid(row=2, columnspan=2, pady=10)
encode_result_label = tk.Label(encode_frame, text="Encoded LSB & MSB: ")
encode_result_label.grid(row=3, columnspan=2)

app.mainloop()
