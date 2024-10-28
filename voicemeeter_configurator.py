import customtkinter as ctk
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from tkinter import filedialog, messagebox

def generate_config():
    try:
        root = Element("VoicemeeterConfig")

        hardware_out = SubElement(root, "HardwareOut")
        a1 = SubElement(hardware_out, "A1")
        a1.text = "Speakers"
        mic_settings = SubElement(root, "MicSettings")

        
        noise_gate = SubElement(mic_settings, "NoiseGate")
        noise_gate.set("threshold", str(noise_gate_threshold.get()))
        noise_gate.set("attack", str(noise_gate_attack.get()))
        noise_gate.set("release", str(noise_gate_release.get()))


        compressor = SubElement(mic_settings, "Compressor")
        compressor.set("ratio", compressor_ratio.get())
        compressor.set("threshold", str(compressor_threshold.get()))
        compressor.set("attack", str(compressor_attack.get()))
        compressor.set("release", str(compressor_release.get()))

        
        equalizer = SubElement(mic_settings, "Equalizer")
        eq_low = SubElement(equalizer, "Low")
        eq_low.set("gain", str(eq_low_gain.get()))
        eq_mid = SubElement(equalizer, "Mid")
        eq_mid.set("gain", str(eq_mid_gain.get()))
        eq_high = SubElement(equalizer, "High")
        eq_high.set("gain", str(eq_high_gain.get()))

        
        high_pass = SubElement(equalizer, "HighPassFilter")
        high_pass.set("cutoff_frequency", str(high_pass_cutoff.get()))
        high_pass.set("slope", "12dB")

        
        buffering = SubElement(root, "Buffering")
        buffering.set("latency", "128")

        
        file_path = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
        if file_path:
           
            rough_string = tostring(root, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            with open(file_path, "w") as file:
                file.write(reparsed.toprettyxml(indent="  "))
            messagebox.showinfo("Success", "Configuration file created successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Voicemeeter Configurator")
root.geometry("450x740")
noise_gate_frame = ctk.CTkFrame(root)
noise_gate_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(noise_gate_frame, text="Noise Gate Settings", font=("Arial", 16)).pack(anchor="w", padx=10, pady=5)
noise_gate_threshold = ctk.CTkSlider(noise_gate_frame, from_=0, to=100, number_of_steps=100)
noise_gate_threshold.set(25)
ctk.CTkLabel(noise_gate_frame, text="Threshold").pack(anchor="w", padx=10)
noise_gate_threshold.pack(fill="x", padx=20)
noise_gate_attack = ctk.CTkSlider(noise_gate_frame, from_=0, to=10, number_of_steps=100)
noise_gate_attack.set(1)
ctk.CTkLabel(noise_gate_frame, text="Attack").pack(anchor="w", padx=10)
noise_gate_attack.pack(fill="x", padx=20)
noise_gate_release = ctk.CTkSlider(noise_gate_frame, from_=0, to=500, number_of_steps=100)
noise_gate_release.set(100)
ctk.CTkLabel(noise_gate_frame, text="Release").pack(anchor="w", padx=10)
noise_gate_release.pack(fill="x", padx=20)
compressor_frame = ctk.CTkFrame(root)
compressor_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(compressor_frame, text="Compressor Settings", font=("Arial", 16)).pack(anchor="w", padx=10, pady=5)
compressor_ratio = ctk.StringVar(value="3:1")
compressor_ratio_dropdown = ctk.CTkOptionMenu(compressor_frame, variable=compressor_ratio, values=["1:1", "2:1", "3:1", "4:1", "6:1"])
compressor_ratio_dropdown.pack(fill="x", padx=20, pady=5)
compressor_threshold = ctk.CTkSlider(compressor_frame, from_=0, to=20, number_of_steps=100)
compressor_threshold.set(8)
ctk.CTkLabel(compressor_frame, text="Threshold").pack(anchor="w", padx=10)
compressor_threshold.pack(fill="x", padx=20)

compressor_attack = ctk.CTkSlider(compressor_frame, from_=0, to=10, number_of_steps=100)
compressor_attack.set(3)
ctk.CTkLabel(compressor_frame, text="Attack").pack(anchor="w", padx=10)
compressor_attack.pack(fill="x", padx=20)

compressor_release = ctk.CTkSlider(compressor_frame, from_=0, to=500, number_of_steps=100)
compressor_release.set(200)
ctk.CTkLabel(compressor_frame, text="Release").pack(anchor="w", padx=10)
compressor_release.pack(fill="x", padx=20)

equalizer_frame = ctk.CTkFrame(root)
equalizer_frame.pack(pady=10, padx=10, fill="x")
ctk.CTkLabel(equalizer_frame, text="Equalizer Settings", font=("Arial", 16)).pack(anchor="w", padx=10, pady=5)
eq_low_gain = ctk.CTkSlider(equalizer_frame, from_=-10, to=10, number_of_steps=100)
eq_low_gain.set(-3)
ctk.CTkLabel(equalizer_frame, text="Low Gain").pack(anchor="w", padx=10)
eq_low_gain.pack(fill="x", padx=20)
eq_mid_gain = ctk.CTkSlider(equalizer_frame, from_=-10, to=10, number_of_steps=100)
eq_mid_gain.set(3)
ctk.CTkLabel(equalizer_frame, text="Mid Gain").pack(anchor="w", padx=10)
eq_mid_gain.pack(fill="x", padx=20)
eq_high_gain = ctk.CTkSlider(equalizer_frame, from_=-10, to=10, number_of_steps=100)
eq_high_gain.set(-1)
ctk.CTkLabel(equalizer_frame, text="High Gain").pack(anchor="w", padx=10)
eq_high_gain.pack(fill="x", padx=20)
ctk.CTkLabel(root, text="High-Pass Filter Cutoff Frequency", font=("Arial", 16)).pack(anchor="w", padx=10, pady=(10, 0))
high_pass_cutoff = ctk.CTkSlider(root, from_=20, to=200, number_of_steps=180)
high_pass_cutoff.set(80)
high_pass_cutoff.pack(fill="x", padx=20)
generate_button = ctk.CTkButton(root, text="Generate Config", command=generate_config)
generate_button.pack(pady=20)
root.mainloop()
