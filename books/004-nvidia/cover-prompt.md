# Cover design prompt: The NVIDIA Moat

Use this prompt to generate a professional book cover for "The NVIDIA Moat: How One Company Built the Foundation Beneath Artificial Intelligence" by Daniel Paredes.

---

## Prompt for image generation agent

Create a professional non-fiction book cover for a deep analytical book about NVIDIA Corporation, the semiconductor and AI infrastructure company. The book covers NVIDIA's transformation from a 1993 gaming graphics startup into the most valuable semiconductor company in history, with particular focus on the CUDA software moat, GPU architecture evolution, and the company's central role in the AI revolution.

### Visual concept

The cover should evoke the themes of layers, foundations, and infrastructure. The central visual metaphor is a layered or stacked motif representing the technology stack that NVIDIA has built: hardware at the base (silicon, GPU die patterns), software in the middle (CUDA, represented by abstract code or parallel processing lines), and AI at the top (neural network node patterns emerging upward). The "moat" concept should be subtly conveyed through a protective or encircling element, like concentric rings or a fortress-like geometry around the central stack.

### Color palette

- **Primary:** NVIDIA green (#76b900). Use this as the dominant accent color for the central visual element. It should feel vibrant and technological, immediately recognizable to anyone who knows the brand without using the logo.
- **Accent:** Deep dark blue-black (#1a1a2e). Use this as the dominant background. It should feel authoritative, deep, and serious, like the dark of a data center.
- **Supporting:** White or very light gray for text. Subtle lighter green or teal for secondary visual details. Avoid bright colors beyond the green accent.

### Composition

- **Upper portion:** The title "The NVIDIA Moat" in large, clean serif typography (think Linux Libertine or similar). White or very light text against the dark background.
- **Center:** The layered visual element. This could be abstract GPU die geometry (rectangular grids, silicon patterns) at the base, flowing upward into parallel lines or neural network connections. The green accent should illuminate key nodes or edges, like circuit traces glowing in the dark.
- **Lower portion:** The subtitle "How One Company Built the Foundation Beneath Artificial Intelligence" and author name "Daniel Paredes" in smaller, clean sans-serif type.

### Typography

- Title: Serif, elegant but modern. Not decorative or ornate.
- Subtitle: Sans-serif, lighter weight, clearly subordinate to the title.
- Author name: Sans-serif, same weight as subtitle or slightly bolder.
- No italics on the title. No quotation marks around the title.

### Mood

- Authoritative and analytical. This is a serious deep-dive analysis, not a lightweight business book.
- Technologically sophisticated. The reader should immediately sense this is about silicon, compute infrastructure, and the hardware layer beneath AI.
- Clean and minimal. Avoid clutter. The cover should read well as a thumbnail on Leanpub and Amazon.
- Slightly dark and dramatic. The dark background with green glowing elements should evoke a data center or server room aesthetic.

### What to avoid

- Do not use the NVIDIA logo or any trademarked company branding.
- Do not use photographs of products, GPUs, or people.
- Do not use generic stock imagery (handshakes, globes, ascending arrows, robots).
- Do not make it look like a textbook or academic paper.
- Do not use more than three colors (dark background, green accent, white/light gray text).
- Do not add gradients or gloss effects. Keep it flat and modern.

### Reference style

Think of the visual style of Princeton University Press or MIT Press economics/technology books: clean, geometric, confident, restrained. The cover should feel like it belongs in a serious library, not on an airport bookstore impulse-buy rack.

### Technical specs

- Aspect ratio: US Letter (8.5 x 11 inches, which is 1:1.294 ratio). Request this explicitly.
- Resolution: at least 300 DPI for print. In pixels at 150 DPI: 1275 x 1650.
- Format: JPG or PNG
- The cover will be rendered in PDF and displayed on screen, so it needs to work at both full size and thumbnail size.

### Cover dimension fix

After generating the image, check its actual dimensions with `sips -g pixelWidth -g pixelHeight <file>`. If the ratio does not match US Letter (1:1.294), pad the sides using ImageMagick: `magick <input> -background "<HEX_COLOR>" -gravity center -extent <target_width>x<height> cover-padded.png`. Calculate target width as `height * 8.5 / 11`. The background color must match the image's actual background exactly. Ask the user to sample it with a color picker and provide the hex code. Store the sampled color in `metadata.yaml` as `cover_bg_color: "<HEX>"` so the cover can be regenerated without re-sampling. Do NOT assume the metadata `pdf.colors.primary` matches the actual image background. Then convert to JPEG: `sips -s format jpeg cover-padded.png --out images/cover.jpg`. Never stretch or crop.

### Summary in one sentence

A deep dark blue-black book cover with glowing NVIDIA-green silicon and neural network geometry, clean serif title typography, and a data center aesthetic that communicates serious analytical depth about GPU infrastructure and the AI revolution.
