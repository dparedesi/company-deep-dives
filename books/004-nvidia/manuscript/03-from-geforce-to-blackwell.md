# Chapter 3: From GeForce to Blackwell

The story of NVIDIA's ascent to AI dominance is not merely a story of clever marketing or fortunate timing. It is a story of relentless architectural innovation spanning two decades. Each GPU generation represented a calculated bet on where computing was heading, with some bets paying off spectacularly and others nearly bankrupting the company. From the early Tesla architecture through the latest Blackwell generation, NVIDIA maintained a cadence of annual architecture updates that consistently delivered performance improvements and new capabilities.

This generational ladder is the engine of NVIDIA's competitive position. Understanding each generation, what changed, why it mattered, and how the market received it, is essential to understanding how NVIDIA became the most valuable company in history.

## Tesla architecture: the unified shader foundation (2006)

The Tesla architecture, introduced in 2006 with the G80 core, established the template for modern GPUs. Before Tesla, GPUs had separate pipelines for vertex processing, geometry processing, and pixel processing. This fixed-function architecture was efficient for graphics but inflexible for general-purpose computing. Tesla introduced unified shaders, which allowed the same computational units to handle any type of graphics operation.

This flexibility was essential for CUDA, which NVIDIA would launch the following year. Unified shaders meant that CUDA could treat the GPU as a general-purpose parallel processor without worrying about which hardware units were available for computation. The entire GPU became available for compute workloads.

The GeForce 8800 GTX, based on Tesla, featured 128 CUDA cores organized into streaming multiprocessors. Each streaming multiprocessor contained a set of CUDA cores, special function units, and a shared memory bank. This organization became the basic template for future GPU architectures. The 8800 GTX delivered 518 gigaflops of single-precision performance, a dramatic increase over the previous generation.

What made Tesla significant was not its raw performance but its programmability. The G80 core supported the CUDA compute model, which allowed developers to write parallel programs that executed on the GPU. This was a radical departure from previous GPU programming models, which required programmers to express their computations as graphics operations.

Tesla also introduced the memory hierarchy that would define GPU programming. Global memory provided large capacity but high latency. Shared memory provided fast access for data sharing between threads in a block. Registers provided the fastest access but were limited in quantity. This hierarchy allowed programmers to optimize their code based on access patterns.

The Tesla architecture shipped in 90nm manufacturing process. The GeForce 8800 GTX had 681 million transistors and consumed 177 watts of power. This power consumption was high but acceptable for a high-end graphics card. However, it foreshadowed the thermal challenges that would plague later architectures.

## Fermi architecture: the overheating crisis (2010)

Fermi, launched in 2010 with the GF100 core, was the first architecture designed from the ground up for CUDA as well as graphics. It featured 512 CUDA cores organized into 16 streaming multiprocessors. Each streaming multiprocessor contained 32 CUDA cores, four times the previous generation. This dramatic increase in core count promised substantial performance improvements.

Fermi introduced a configurable L1 and shared memory hierarchy. Programmers could configure the 64KB of on-chip memory as 48KB of shared memory plus 16KB of L1 cache, or 16KB of shared memory plus 48KB of L1 cache. This flexibility allowed programmers to optimize for their specific workloads. Compute-bound applications could use more shared memory. Memory-bound applications could use more cache.

Fermi was the first architecture to support ECC memory for error correction in data center environments. ECC memory detects and corrects bit flips that can occur in memory, which is essential for reliable long-running computations in data centers. This made Fermi suitable for high-performance computing applications.

Fermi was also the first architecture to support NVIDIA's NVLink interconnect for high-speed GPU-to-GPU communication, although this feature would not appear in products until later generations. The architectural foundation was laid in Fermi.

However, Fermi became notorious for its thermal and power problems. The GF100 chip was massive, measuring 529 square millimeters on TSMC's 40nm process. It contained 3 billion transistors. This large chip size and high transistor count resulted in significant power consumption and heat generation.

The GeForce GTX 480, the flagship consumer card based on Fermi, consumed 250 watts of power and reached 95 degrees Celsius under load. The fan had to spin at maximum speed to keep the card from overheating, resulting in unacceptable noise levels. Reviewers criticized the GTX 480 for its heat and power consumption, which were significantly higher than competing cards from AMD.

The Fermi overheating crisis nearly killed NVIDIA's data center ambitions. Enterprise customers were reluctant to deploy GPUs that consumed so much power and generated so much heat. Data centers had strict power budgets, and thermal management was a significant operational cost. A GPU that consumed 250 watts required more cooling and more power infrastructure than competitors' offerings.

NVIDIA responded to the Fermi crisis with a mid-cycle refresh. The GF110 variant, which powered the GeForce GTX 580, reduced power consumption and improved thermals through improved power gating and more mature manufacturing. The GTX 580 consumed 244 watts, a modest improvement, but ran significantly cooler thanks to optimized vapor chamber cooling.

The Fermi experience taught NVIDIA important lessons about power efficiency and thermal design. These lessons would shape the next several generations of GPU architecture. NVIDIA's competitors seized on Fermi's problems, marketing their own cards as more power-efficient alternatives. It would take several years for NVIDIA to fully recover its reputation in this area.

## Kepler architecture: the energy efficiency revolution (2012)

Kepler, introduced in 2012 with the GK104 core, represented NVIDIA's response to the Fermi crisis. The design goal was explicit: deliver more performance with less power. Kepler succeeded dramatically, establishing NVIDIA's leadership in performance per watt.

The GeForce GTX 680, based on Kepler, delivered performance comparable to the previous generation's GTX 580 while consuming significantly less power. The GTX 680 had a 195 watt TDP, compared to the GTX 580's 244 watts. This 20% reduction in power consumption came with improved performance in many workloads, representing a dramatic improvement in performance per watt.

Kepler achieved this efficiency through several architectural innovations. First, it reduced the clock speed of individual CUDA cores but increased the total number of cores. The GK104 chip had 1536 CUDA cores organized into 8 streaming multiprocessors. Each streaming multiprocessor contained 192 CUDA cores, organized as 6 groups of 32 cores. This organization allowed more work to be done in parallel at lower clock speeds, reducing power consumption.

Second, Kepler introduced GPU Boost, which allowed the GPU to dynamically adjust its clock speed based on power and thermal headroom. If the GPU was running cool and had power headroom, it could increase its clock speed beyond the base frequency. If the GPU was running hot or approaching its power limit, it could reduce clock speed to stay within safe operating parameters. This allowed the GPU to deliver optimal performance in real-world usage scenarios where the GPU was not constantly at maximum utilization.

GPU Boost was a significant innovation because it acknowledged the reality of GPU workloads. Games and applications do not always use the GPU's full capabilities. During light usage periods, the GPU could boost clock speeds to deliver higher frame rates. During heavy usage periods, it could reduce clock speeds to stay within thermal and power limits. This dynamic optimization improved both performance and efficiency.

Third, Kepler improved the memory subsystem. The GTX 680 used GDDR5 memory at 6 Gbps, providing 192 GB/s of memory bandwidth. The memory controller was redesigned for better efficiency, reducing the power consumption of memory accesses.

Fourth, Kepler introduced a new texture cache architecture. The texture units were reorganized to improve efficiency and reduce power consumption. Texture filtering operations were optimized to use less power while maintaining quality.

The Kepler architecture also introduced bindless textures, a feature that allowed shaders to access textures without being explicitly bound to texture units. This improved programming flexibility and reduced CPU overhead for texture management.

The efficiency improvements in Kepler had significant market implications. Enterprise customers, who had been reluctant to adopt Fermi due to its power consumption, were more willing to deploy Kepler-based GPUs. The Tesla K20 GPU, based on Kepler, became a popular choice for high-performance computing clusters. Its 225 watt TDP was manageable in data center environments, and its performance per watt was competitive with CPUs and other accelerators.

Kepler's efficiency revolution was essential for NVIDIA's data center ambitions. As AI workloads began to emerge, the ability to deliver high performance with acceptable power consumption became critical. Training deep neural networks required substantial compute resources, but data centers had limited power budgets. Kepler's efficiency made GPU-based AI training feasible at scale.

The success of Kepler established a pattern that would continue through subsequent generations: each architecture would deliver substantial improvements in performance per watt. This focus on efficiency became a core part of NVIDIA's architectural philosophy, driven in part by the lessons learned from the Fermi crisis.

## Maxwell architecture: the dark horse that exceeded expectations (2014)

Maxwell, launched in 2014 with the GM204 core, was not initially positioned as a flagship architecture. It was designed as a mid-range chip that would complement a larger flagship chip. However, the larger GM200 chip was delayed, and NVIDIA released the GM204 as the GeForce GTX 980. This accident of product strategy became one of NVIDIA's most successful architectures.

The GeForce GTX 980 delivered approximately twice the performance of the GTX 680 at the same power level. This dramatic improvement in performance per watt came primarily from architectural optimization rather than process technology alone. Both Kepler and Maxwell were manufactured on TSMC's 28nm process, so the efficiency gains were not from manufacturing improvements.

Maxwell achieved its efficiency through several innovations. First, it redesigned the streaming multiprocessor architecture. Maxwell streaming multiprocessors had 128 CUDA cores organized into 4 groups of 32 cores. This was a reduction from Kepler's 192 cores per streaming multiprocessor, but the individual cores were more efficient. The streaming multiprocessor design was optimized for real-world workloads, reducing power consumption while maintaining or improving performance.

Second, Maxwell introduced VRAM compression. Graphics data often contains redundant information. For example, a sky texture might have large regions of similar colors. Maxwell could compress this data before storing it in video memory, reducing the memory bandwidth requirements. Since memory bandwidth is often a bottleneck for graphics performance, reducing bandwidth requirements allowed the GPU to deliver better performance without consuming more power.

Third, Maxwell improved the dynamic clock scaling introduced in Kepler. The GPU could adjust its clock speed more precisely based on workload, staying at optimal frequencies more often. This reduced power consumption during light usage and allowed higher boost clocks during heavy usage.

Fourth, Maxwell improved the power delivery system. The voltage regulation module was redesigned for better efficiency, reducing power loss in voltage conversion. The GPU could operate at lower voltages while maintaining stability, further reducing power consumption.

The GeForce GTX 980 had a 165 watt TDP, significantly lower than the GTX 680's 195 watt TDP while delivering substantially better performance. The GTX 970, a cut-down variant, became one of the best-selling GPUs of all time due to its excellent price to performance ratio.

Maxwell's efficiency made it popular for cryptocurrency mining. Ethereum mining, which became popular in 2016, was particularly well-suited to Maxwell GPUs due to their excellent performance per watt. Miners built large arrays of GTX 970 and GTX 980 cards, creating secondary market demand that drove up prices.

The efficiency of Maxwell also had implications for data center deployment. The Tesla M40 and M60 GPUs, based on Maxwell, were used for inference and virtualization workloads. Their low power consumption made them suitable for dense deployment in data center racks.

Maxwell's success as a "dark horse" architecture taught NVIDIA an important lesson: architectural optimization could deliver gains as large as process node shrinks. While the industry was racing to smaller manufacturing nodes, NVIDIA demonstrated that smart design could deliver comparable efficiency improvements on the same process node.

## Pascal architecture: the first real data center push (2016)

Pascal, introduced in 2016 with the GP100 core, marked the transition to 16nm FinFET manufacturing. This process node shrink delivered significant improvements in power efficiency and clock speeds. But more importantly, Pascal represented NVIDIA's first serious push into the data center market for AI and high-performance computing.

The GeForce GTX 1080 brought GDDR5X memory, which dramatically increased memory bandwidth. GDDR5X was an evolution of GDDR5 that ran at higher clock speeds. The GTX 1080's memory ran at 10 Gbps, providing 320 GB/s of memory bandwidth compared to the GTX 980's 224 GB/s. This additional bandwidth was essential for high-resolution gaming and compute workloads.

Pascal introduced simultaneous multi-projection (SMP), which accelerated virtual reality rendering. In VR, each eye needs a slightly different view of the scene. Traditional rendering would render each view separately, effectively doubling the rendering workload. SMP could generate multiple views in a single pass, reducing the VR rendering overhead. This made Pascal GPUs attractive for VR applications.

The GP102 variant powered the Titan Xp, NVIDIA's flagship consumer GPU. The Titan Xp featured 3584 CUDA cores and 12GB of GDDR5X memory. It was positioned as the ultimate gaming GPU, with a price tag of $1,200. The Titan series established a pricing tier for enthusiasts who wanted the absolute best performance regardless of cost.

But the most significant impact of Pascal was in the data center. The Tesla P100 based on GP100 was the first GPU specifically designed for AI and high-performance computing. While previous Tesla products had been based on consumer GPUs with minor modifications, the P100 was designed from the ground up for compute workloads.

The Tesla P100 featured 3584 CUDA cores and 16GB of HBM2 memory. HBM (High Bandwidth Memory) was a new memory technology that stacked memory dies vertically and connected them to the GPU through a wide interface. The P100 had a 4096-bit memory interface delivering 720 GB/s of memory bandwidth, more than double the GTX 1080's bandwidth.

The P100 also introduced NVLink, NVIDIA's high-speed GPU-to-GPU interconnect. Each P100 GPU had four NVLink connections, each delivering 20 GB/s of bandwidth. This was dramatically faster than PCIe 3.0, which delivered approximately 12 GB/s of bandwidth. NVLink allowed GPUs to share data more efficiently, which was essential for multi-GPU training of neural networks.

The P100 was priced at approximately $5,000 for the PCIe card and $10,000 for the SXM2 version. The SXM2 form factor was a mezzanine card that mounted directly on a system board, allowing better power delivery and cooling. SXM2 GPUs also had higher TDPs and clock speeds than PCIe cards.

The Tesla P40, another Pascal-based data center GPU, was optimized for inference. It had 24GB of GDDR5X memory and INT8 (8-bit integer) operations for low-precision inference. Integer operations consumed less power and delivered higher throughput than floating-point operations, making them suitable for inference workloads where lower precision was acceptable.

Pascal's data center push established the template for future generations. Each generation would have a flagship consumer GPU for gaming, a Titan variant for enthusiasts, and Tesla variants optimized for training and inference. This segmentation allowed NVIDIA to address different market segments with products optimized for their specific needs.

The timing of Pascal's release was fortuitous. AI was beginning to emerge as a major workload. The AlexNet breakthrough had occurred in 2012, and by 2016, deep learning was gaining mainstream adoption in tech companies. The Tesla P100 became the GPU of choice for AI research, and NVIDIA's data center revenue began to grow rapidly.

## Volta architecture: Tensor Cores as the biggest innovation since CUDA (2017)

Volta, introduced in 2017 with the GV100 core, represented the most significant architectural innovation in NVIDIA's history since the introduction of CUDA. Volta introduced Tensor Cores, specialized processing units designed for the matrix operations that dominate deep learning workloads.

Before Volta, GPUs performed deep learning computations using their CUDA cores. CUDA cores were designed for general-purpose parallel computing and could handle matrix operations, but they were not optimized for the specific mathematical patterns of neural networks. Tensor Cores changed this by specializing in matrix multiply and accumulate operations.

A typical neural network layer involves multiplying an input matrix by a weight matrix and adding a bias. This is matrix multiplication, and it represents the bulk of the computational work in deep learning. Traditional CUDA cores handle these operations using standard floating-point arithmetic. Tensor Cores are designed specifically for matrix operations. They can execute a 4x4 matrix multiply and accumulate in a single clock cycle, where the input matrices are in FP16 and the accumulation happens in FP32. This provides up to eight times the throughput of FP32 operations on CUDA cores for appropriate workloads.

The Tesla V100 data center GPU featured 640 Tensor Cores delivering 125 TFLOPS of deep learning performance. This was a dramatic leap forward for AI training. Where the P100 could deliver approximately 20 TFLOPS of FP16 performance, the V100 delivered 125 TFLOPS of Tensor Core performance. This 6x performance improvement enabled training of larger models and faster experimentation.

Volta also introduced improvements to the CUDA core architecture. The GV100 chip had 5120 CUDA cores organized into 84 streaming multiprocessors. The memory subsystem was enhanced with 32GB of HBM2 memory delivering 900 GB/s of memory bandwidth. The chip was manufactured on TSMC's 12nm FFN process, measuring 815 square millimeters and containing 21.1 billion transistors.

The significance of Tensor Cores cannot be overstated. They represented the divergence of GPU architectures from pure graphics. In a graphics-only architecture, area and power are dedicated to texture units, render outputs, and other graphics-specific functions. In an AI-optimized architecture, those resources are reallocated to Tensor Cores. This specialization delivered enormous performance for AI but came at the cost of flexibility. Tensor Cores were excellent for neural networks but less useful for other types of computation.

Volta was the first architecture that was clearly designed for AI as a primary workload, with graphics as a secondary consideration. The Tesla V100 had no video outputs and could not display graphics. It was purely a compute accelerator. This signaled NVIDIA's strategic shift toward AI as the primary growth driver for the company.

The introduction of Tensor Cores created a performance gap that competitors struggled to close. AMD and Intel could match CUDA core performance, but without equivalent specialized hardware for AI workloads, they could not compete on deep learning performance. This gap would widen with subsequent generations as NVIDIA refined Tensor Core capabilities.

The V100 became the workhorse of the AI boom. Researchers training large language models, computer vision systems, and recommendation systems all relied on V100 GPUs. The GPU's ability to train models in days rather than weeks accelerated AI research dramatically. NVIDIA's data center revenue grew from $839 million in fiscal 2017 to $1.5 billion in fiscal 2018, driven largely by Volta demand.

## Turing architecture: ray tracing as a consumer technology bet (2018)

Turing, launched in 2018 with the TU102 core, brought RT Cores for real-time ray tracing. Ray tracing simulates the physical behavior of light, creating more realistic lighting, shadows, and reflections. The technique had been used in film and television for years but was too computationally expensive for real-time rendering in games.

RT Cores accelerated ray tracing by handling the traversal of bounding volume hierarchies (BVH). BVH is a data structure that organizes geometry in a scene to accelerate ray intersection tests. Instead of testing every triangle in a scene, the BVH allows the system to quickly determine which objects a ray might intersect. RT Cores accelerated this traversal operation, making real-time ray tracing feasible.

The RTX 2080 Ti, the flagship Turing card, featured 4352 CUDA cores, 576 Tensor Cores, and 68 RT Cores. It had 11GB of GDDR6 memory delivering 616 GB/s of bandwidth. The GPU was priced at $999, establishing a premium price point for ray tracing-capable hardware.

Turing also introduced improved Tensor Cores that supported INT4 and INT8 operations. These lower precision modes were useful for inference where reduced precision could be used without significant accuracy loss. INT8 operations delivered twice the throughput of FP16 operations, and INT4 delivered four times the throughput. This made Turing GPUs excellent for inference workloads.

The Turing launch was controversial. Ray tracing was a new technology, and there were few games that supported it at launch. The performance impact of ray tracing was substantial, often reducing frame rates by 50% or more. Critics questioned why gamers should pay premium prices for hardware that had no immediate benefit.

NVIDIA's bet was that ray tracing would become a standard feature in future games, and that early adopters would benefit from being ahead of the curve. This bet proved correct. As of 2025, more than 500 games support ray tracing, and the technology has become a selling point for PC gaming.

The controversy around Turing also highlighted NVIDIA's challenge of justifying premium pricing. The RTX 2080 Ti was significantly more expensive than the previous generation's GTX 1080 Ti, but the performance improvement in traditional rasterization was modest. Gamers who did not care about ray tracing or AI features questioned the value proposition.

However, Turing introduced DLSS (Deep Learning Super Sampling), which used Tensor Cores to increase frame rates. In DLSS, the GPU renders at a lower resolution, and an AI model upscales the image to the target resolution. This is faster because rendering fewer pixels is less work. DLSS 1, introduced with Turing, used spatial upscaling and delivered mixed results. DLSS 2, introduced later with Ampere, used temporal information and delivered much better quality.

Turing established the RTX brand, which replaced the GTX brand for high-end GPUs. RTX indicated the presence of Tensor Cores and RT Cores, signifying that the GPU was capable of AI and ray tracing features. GTX branding continued for lower-end GPUs without these features.

## Ampere architecture: the COVID, crypto, and AI perfect storm (2020)

Ampere, introduced in 2020 with the GA100 core, arrived at a unique moment in history. The COVID-19 pandemic drove demand for PC hardware as people worked from home, gamed more, and invested in cryptocurrency. At the same time, AI adoption was accelerating as enterprises sought to automate processes and gain insights from data.

Ampere brought second-generation Tensor Cores with sparse matrix acceleration. Sparse matrix acceleration takes advantage of the fact that many matrices in neural networks have mostly zero values. By skipping calculations on zeros, Ampere could double throughput for certain workloads. This feature was particularly useful for large language models, which often had sparse weight matrices.

The A100 data center GPU featured 6912 CUDA cores and 432 Tensor Cores. It supported up to 80GB of HBM2e memory delivering 2 TB/s of memory bandwidth. The chip was manufactured on TSMC's 7nm process, measuring 826 square millimeters and containing 54.2 billion transistors.

The A100 introduced MIG (Multi-Instance GPU) capability, which allowed a single A100 to be partitioned into seven independent instances. Each instance had its own CUDA cores, memory, and cache. This improved GPU utilization in cloud environments where multiple users or applications shared a GPU. Rather than leaving a GPU idle while one user's job ran, MIG allowed seven smaller jobs to run simultaneously.

The RTX 30 series for consumers brought DLSS 2.0, an AI upscaling technology that used Tensor Cores to increase frame rates and resolution. DLSS 2 used temporal information from previous frames to improve quality, addressing the shortcomings of DLSS 1. The result was upscaling that was often indistinguishable from native rendering, with substantial performance improvements.

The RTX 3080, the flagship consumer Ampere card, delivered approximately twice the performance of the previous generation's RTX 2080 at similar pricing. However, the launch was characterized by extreme supply shortages. Scalpers bought inventory and resold at multiples of the MSRP. Cryptocurrency miners, seeking GPUs for Ethereum mining, further constrained supply. Gamers struggled to find RTX 30 series cards at reasonable prices.

The GPU shortage persisted through most of 2021 and 2022. NVIDIA's revenue grew dramatically as it shipped as many GPUs as it could manufacture, but the company also faced criticism for not doing enough to ensure cards reached gamers. NVIDIA introduced cryptocurrency hash rate limiters on some cards to discourage mining, but these measures were easily bypassed.

The A100 became the workhorse of enterprise AI deployments. Its high memory bandwidth and large memory capacity made it suitable for training large language models. Companies like OpenAI, Anthropic, and Meta used A100 GPUs to train models like GPT-3, Claude, and LLaMA. The A100's performance and reliability made it the default choice for AI infrastructure.

Ampere also established the pattern of separate silicon for consumer and data center markets. The GA100 chip used for data center products was different from the GA102 chip used for consumer products. This separation allowed NVIDIA to optimize each design for its target market. Data center GPUs prioritized memory bandwidth and compute. Consumer GPUs prioritized rasterization performance and features.

The Ampere generation coincided with the beginning of the generative AI boom. When DALL-E and ChatGPT launched in 2021 and 2022, they ran on A100 GPUs. The success of these applications drove massive demand for NVIDIA data center GPUs. NVIDIA's data center revenue grew from $2.9 billion in fiscal 2020 to $6.7 billion in fiscal 2022.

## Hopper architecture: H100 as the most important chip in AI history (2022)

Hopper, launched in 2022 with the GH100 core, was designed for exascale AI and high-performance computing. The H100 GPU introduced the Transformer Engine, which optimized the mixed-precision calculations used in transformer models. Transformers had become the dominant architecture for large language models, and the Transformer Engine delivered dramatic performance improvements for this workload.

The Transformer Engine automatically manages precision during transformer model training. It uses FP8 (8-bit floating point) for calculations where possible to improve throughput, and FP16 for calculations where higher precision is required. This dynamic precision management delivers better performance than manual precision tuning while maintaining model accuracy.

The H100 GPU delivered up to 30 times the performance of the previous generation for AI inference. This performance improvement came from multiple factors: higher clock speeds, more Tensor Cores, FP8 support, and the Transformer Engine. For transformer model inference, the H100 could process requests much faster than the A100, reducing latency and improving user experience for applications like ChatGPT.

The H100 had 132 streaming multiprocessors containing 16,896 CUDA cores and 528 Tensor Cores. It supported up to 188GB of HBM3 memory delivering 3.35 TB/s of memory bandwidth. The chip was manufactured on TSMC's 4N process (a customized version of 4nm), measuring 814 square millimeters and containing 80 billion transistors.

The H100's introduction coincided with the generative AI boom triggered by ChatGPT's launch in November 2022. Demand for AI training and inference infrastructure exploded. H100 GPUs became the most sought-after accelerators for AI workloads, with secondary market prices reaching $40,000 or more per GPU.

The H100's performance advantages over the A100 were substantial. For GPT-3 training, the H100 was approximately 4x faster than the A100. For inference, the H100 was up to 30x faster for certain workloads. This performance improvement allowed AI companies to train larger models and serve more users with fewer GPUs.

The H100 also introduced improved NVLink bandwidth. Fourth-generation NVLink delivered 45 GB/s per link, compared to 25 GB/s in the previous generation. Each H100 SXM5 GPU had 18 NVLink links, delivering up to 900 GB/s of GPU-to-GPU bandwidth. This high-bandwidth connectivity was essential for efficient multi-GPU training.

The H100 became the standard for AI infrastructure. Microsoft, Google, Meta, OpenAI, Anthropic, xAI, and other leading AI companies deployed thousands of H100 GPUs for training large language models. The GPU's performance and reliability made it the foundation of the AI industry. H100 demand exceeded supply through 2023 and 2024, creating NVIDIA's historic revenue growth.

The success of the H100 established NVIDIA's position as the most valuable company in the world. NVIDIA's market capitalization surpassed $2 trillion in 2024, driven largely by H100 demand. The GPU that had been designed for AI and HPC workloads became the engine of the AI revolution.

Hopper also introduced confidential computing capabilities, which encrypted data in use on the GPU. This allowed sensitive data to be processed without exposing it to the host system or cloud provider. Confidential computing addressed regulatory and privacy concerns in industries like healthcare and finance.

## Blackwell architecture: designed for the age of AI reasoning (2024)

Blackwell, introduced in 2024, is named after David Blackwell, a mathematician who made fundamental contributions to game theory and statistics. The GB200 GPU architecture is designed for the "age of AI reasoning," emphasizing inference performance for large language models rather than just training performance.

Blackwell features next-generation Tensor Cores with FP4 (4-bit floating point) support. FP4 allows even lower precision computations than FP8, further increasing throughput for inference workloads. The architecture supports mixed precision modes including FP4, FP8, FP16, and FP32, allowing developers to optimize for their specific accuracy and performance requirements.

The GB200 NVL72 rack-scale system represents a new form factor for AI infrastructure. It integrates 72 Blackwell GPUs interconnected via NVLink Switch, creating a single logical AI accelerator. All-to-all connectivity delivers 3.6 TB/s of bandwidth per GPU, twice the previous generation. This architecture is optimized for trillion-parameter model inference and training.

The GB200 combines two B200 GPUs with a single Grace CPU into a unified module. The Grace CPU is based on ARM architecture and provides 144 cores with 1.2TB of LPDDR5X memory. The CPU-GPU connection uses NVLink-C2C, a chip-to-chip interconnect that delivers 900 GB/s of bandwidth. This tight integration reduces latency between CPU and GPU, improving performance for inference workloads.

Blackwell also introduces the second-generation Transformer Engine, which further optimizes mixed-precision calculations for transformer models. The engine now supports FP4 training and inference, with automatic precision management to maintain model accuracy. This allows models to be trained faster and deployed with lower latency.

The RAR (Reliability, Availability, and Serviceability) features of Blackwell are designed for data center deployment. The architecture supports live migration of VMs between GPUs, allowing maintenance without downtime. Error detection and correction capabilities have been improved. Power management features allow GPUs to operate at optimal power for their workload.

Blackwell also introduces secure AI capabilities, building on the confidential computing features of Hopper. The architecture includes hardware-based root of trust, secure boot, and encrypted data paths. These features address security and compliance requirements for enterprise AI deployments.

The GB200 NVL72 system is designed for trillion-parameter model inference. A model like GPT-4, which has approximately 1.8 trillion parameters, cannot fit in the memory of a single GPU. The NVL72 system provides 1.5TB of unified GPU memory across 72 GPUs, allowing trillion-parameter models to be loaded entirely in GPU memory. This reduces latency and improves throughput for inference.

Blackwell's emphasis on inference reflects the shifting focus of the AI industry. While training remains important, inference is becoming the dominant workload. As AI models move into production, serving millions of users requires efficient inference infrastructure. Blackwell is optimized for this workload.

Looking forward, the Vera Rubin platform announced at GTC 2025 represents the next generation of AI architecture. Named after the astronomer who pioneered dark matter research, Vera Rubin continues the focus on agentic AI and reasoning-capable computing. The platform extends Blackwell's capabilities with improved networking and further optimizations for the inference workload patterns of large language models.

## The Tensor Core lineage: from Volta to Blackwell

Understanding the Tensor Core's evolution across five generations explains why NVIDIA's lead in AI compute has proven so durable. Each generation refined the same fundamental insight: general-purpose CUDA cores, while flexible, waste silicon and power on workloads that follow predictable mathematical patterns. Matrix multiplication dominates neural network training and inference, and Tensor Cores specialize in exactly that operation.

At the hardware level, a Tensor Core performs a 4x4 matrix multiply and accumulate in a single clock cycle. The input matrices arrive in FP16 (16-bit floating point), while the accumulator operates in FP32 (32-bit), preserving precision where it matters most: the running sum of partial products. This mismatch between input precision and accumulation precision is deliberate. Neural network weights and activations can tolerate lower precision during multiplication, but errors compound during accumulation, so the wider format prevents numerical drift. A single Tensor Core replaces dozens of CUDA core cycles for the same operation, which is why Tensor Core throughput, not CUDA core count, has become the primary metric for AI performance.

The first generation, introduced with Volta in 2017, placed eight Tensor Cores per streaming multiprocessor. The Tesla V100's 640 Tensor Cores delivered 125 TFLOPS of deep learning performance, a figure that dwarfed anything available on competing hardware. Volta's Tensor Cores supported FP16 input and FP32 accumulation, which mapped directly onto the mixed-precision training workflows that researchers were already using. The performance gap was immediate and substantial: workloads that ran for days on Pascal GPUs completed in hours on Volta.

The second generation arrived with Turing in 2018 and broadened the precision envelope. Turing Tensor Cores added INT8 and INT4 integer support alongside the existing FP16 mode. This was not an academic distinction. Inference workloads, where a trained model processes new inputs, can often use lower precision without meaningful accuracy loss because the weights are fixed and the model does not need to learn. INT8 operations delivered twice the throughput of FP16, and INT4 delivered four times the throughput, making Turing GPUs formidable inference accelerators. The timing was fortuitous: as AI companies began deploying models at scale, inference costs started to dominate their compute budgets.

The third generation, launched with Ampere in 2020, introduced two significant advances. Sparse matrix acceleration took advantage of the fact that many neural network weight matrices contain mostly zeros after pruning. By detecting and skipping zero-valued elements, Ampere Tensor Cores could double effective throughput for sparse workloads without any change to the software. Ampere also introduced TF32 (TensorFloat-32), a 19-bit format that maintained the dynamic range of FP32 while using the same hardware datapath as FP16. This meant researchers could train models at nearly FP32 accuracy with the throughput of FP16 hardware, removing the need for manual mixed-precision tuning in many cases.

The fourth generation, delivered with Hopper in 2022, brought the Transformer Engine and FP8 support. The Transformer Engine was a response to the dominance of transformer architectures in large language models. It dynamically switched between FP8 and FP16 precision on a per-layer, per-iteration basis, using FP8 where the layer could tolerate it and falling back to FP16 where higher precision was required. This dynamic precision management was transparent to the user: the hardware and driver stack handled all decisions automatically. The result was up to 30 times the inference performance of the previous generation for transformer workloads, a leap that made Hopper the engine behind the ChatGPT explosion.

The fifth generation, introduced with Blackwell in 2024, extended precision support down to FP4. Four-bit floating point represents an aggressive compression of numerical information, but Blackwell's second-generation Transformer Engine manages the accuracy tradeoff through advanced mixed-precision scheduling. For inference on large language models, FP4 enables substantially higher throughput per watt, which matters when a single deployment might consume hundreds of megawatts. Blackwell Tensor Cores also support new mixed-precision modes that allow developers to fine-tune the balance between accuracy and performance at a granularity that previous generations could not match.

The cumulative effect of five generations of Tensor Core refinement is that NVIDIA's AI performance lead is not simply a matter of building bigger chips. It is a matter of accumulating domain-specific optimizations that compound over time. Each generation's Tensor Cores build on the software infrastructure and programming models established by previous generations. A model trained on Volta can be fine-tuned on Ampere and deployed on Hopper, with each step benefiting from the precision modes and acceleration features unique to that generation. This backward compatibility and forward optimization creates a flywheel: more developers use CUDA because the Tensor Cores are the fastest available, which drives more software investment, which makes the next generation's Tensor Cores even more valuable.

For AI workloads, Tensor Cores matter more than CUDA cores because the bottleneck in neural network computation is almost always matrix multiplication. A GPU with twice the CUDA cores but no Tensor Cores would be slower for training and inference than a GPU with fewer CUDA cores but modern Tensor Cores. This is why NVIDIA's marketing materials lead with Tensor Core performance for data center products and why the competitive benchmark that matters most, MLPerf, measures end-to-end training and inference throughput rather than raw FLOPS from general-purpose compute units.

## Consumer GeForce line evolution alongside data center

While data center GPUs have become NVIDIA's largest business, the GeForce line remains an important market and a source of technological innovation. Gaming technologies developed for GeForce cards often find applications in professional and data center markets.

The GeForce RTX 50 series represents the latest generation of consumer graphics cards. The RTX 5090 is the flagship, based on the Blackwell architecture with the full complement of Tensor Cores and RT Cores. The RTX 5080 offers similar capabilities with slightly reduced specifications. The RTX 5070 family targets the upper-midrange, while the RTX 5060 and RTX 5050 address the mainstream and entry-level segments.

These cards are designed primarily for gaming, where rasterization performance is the priority. But the inclusion of Tensor Cores enables DLSS, and RT Cores enable ray tracing. The gaming and AI capabilities are increasingly intertwined, with AI features becoming standard in gaming GPUs.

The GeForce RTX 40 series, based on the Ada Lovelace architecture, remains in production for many segments. Ada Lovelace is a distinct architecture from Ampere, introducing third-generation RT Cores, fourth-generation Tensor Cores, and the optical flow accelerator that enables DLSS 3 frame generation. The RTX 4090 and RTX 4080 were the high-end Ada cards. The RTX 4070 series addressed the upper-midrange, while the RTX 4060 series targeted mainstream 1080p gaming.

The GTX 16 series, based on the Turing architecture without Tensor Cores or RT Cores, represented a budget-oriented option for gamers who did not care about ray tracing or AI features. This product segmentation allowed NVIDIA to address different price points and customer needs.

The pricing of GeForce GPUs has increased substantially over generations. The flagship GPU has moved from approximately $500 in the Kepler generation to $1,000 in the Ampere generation to $1,600+ for the RTX 4090 and expected $1,999+ for the RTX 5090. This price increase reflects increased manufacturing costs, larger dies, and NVIDIA's market power. However, it also prices some gamers out of the high-end market.

## RTX PRO: the professional workstation

The Quadro brand, which served NVIDIA's professional graphics business for over two decades, was retired in 2020 and replaced with the RTX PRO branding. The rebranding reflected a fundamental shift in the professional visualization market: the features that once differentiated professional GPUs from consumer GPUs, certified drivers, ISV application support, large framebuffers, had become inseparable from the ray tracing and AI capabilities that RTX represented. Quadro was a graphics brand. RTX PRO is a compute brand with graphics capability.

The current RTX PRO portfolio spans the performance spectrum. The RTX PRO 6000 Blackwell sits at the top, offering the full Blackwell GPU with 48GB of GDDR7 memory for professionals who need maximum rendering, simulation, and AI compute performance in a workstation form factor. The RTX PRO 5000 Ada Generation, based on the Ada Lovelace architecture, serves the high-end workstation segment with 32GB of GDDR6 memory. The RTX PRO 4000 addresses mid-range professional visualization needs. The RTX PRO Server extends the product line into data center form factors, providing a universal platform for enterprise AI workloads that benefit from professional-grade GPUs but do not require the full compute density of data center products like the H100.

Professional visualization matters for NVIDIA beyond the direct revenue it generates, which is smaller than gaming or data center but remarkably steady. Enterprise customers buy workstations on predictable three-to-five-year refresh cycles, providing revenue visibility that the more volatile gaming market cannot match. More importantly, professional visualization builds and maintains enterprise relationships. An engineer who uses RTX PRO hardware at work becomes familiar with NVIDIA's software stack, which influences purchasing decisions when that engineer's company needs AI infrastructure. The professional segment is a pipeline into the data center business.

The Omniverse platform represents NVIDIA's most ambitious professional visualization initiative. Built on Pixar's Universal Scene Description (USD) format, Omniverse is a real-time 3D collaboration platform that allows engineers, designers, and architects to work together in shared virtual environments. A car designer in Munich and an aerodynamics engineer in Detroit can simultaneously view and modify the same 3D model, with physics-accurate simulation running in real time. Omniverse supports connections to industry-standard design tools including Autodesk Maya, Siemens NX, and Bentley MicroStation, acting as a universal connector between different software ecosystems.

The platform's digital twin capabilities extend Omniverse from design collaboration into operational simulation. BMW built a digital twin of its factory in Debrecen, Hungary, before the physical factory was constructed. The virtual factory allowed engineers to simulate production flows, identify bottlenecks, and optimize robot placement months before any concrete was poured. NVIDIA has positioned Omniverse as the foundation for "industrial metaverse" applications, where physical systems are mirrored by accurate virtual replicas that update in real time from sensor data. The commercial logic is clear: every factory, warehouse, or facility that builds a digital twin on Omniverse becomes a long-term NVIDIA customer, consuming GPU compute for simulation, rendering, and AI inference on an ongoing basis.

Earth-2 extends NVIDIA's simulation ambitions to planetary scale. Announced as a platform for climate and weather forecasting, Earth-2 combines GPU-accelerated physics models with AI-driven weather prediction to simulate the Earth's atmosphere at resolutions and speeds that traditional numerical weather prediction cannot achieve. The platform uses a combination of physics-based simulation (solving the Navier-Stokes equations for atmospheric dynamics) and AI surrogate models (trained on historical weather data to predict future conditions) to deliver forecasts that update in minutes rather than hours. For industries like agriculture, insurance, and logistics, where weather drives billions of dollars in decisions daily, Earth-2 represents a new category of GPU-accelerated scientific computing.

## RTX 40/50 series and DLSS technology

DLSS (Deep Learning Super Sampling) has evolved through multiple generations and has become a key selling point for RTX cards. The technology uses AI to increase frame rates and resolution, delivering performance improvements of 2 to 4 times at similar quality levels.

DLSS 1, introduced with Turing, used spatial upscaling. It analyzed the current frame only and used a neural network to reconstruct a higher-resolution image. Results were mixed, with some artifacts and inconsistent quality.

DLSS 2, introduced with Ampere, added temporal information. The neural network used data from previous frames to improve reconstruction quality. This addressed many of the quality issues with DLSS 1 and made DLSS a practical technology for gamers.

DLSS 3, introduced with Ada Lovelace, added frame generation. The GPU renders some frames normally, and an AI model generates intermediate frames. This effectively doubles the frame rate, as the GPU only needs to render half the frames. Frame generation works best when the base frame rate is already reasonable, as it adds latency.

DLSS 3.5 added ray reconstruction, using AI to improve ray-traced images. Traditional denoising techniques for ray tracing could introduce artifacts. DLSS 3.5 replaced these denoisers with an AI-based approach that produced cleaner, more accurate images.

DLSS 4 is the latest generation with further quality improvements. It continues the trend of using AI to improve image quality and performance, delivering better results with each generation.

The success of DLSS has important strategic implications for NVIDIA. DLSS requires Tensor Cores, which means it is only available on RTX cards. This creates an upgrade incentive for gamers and justifies the inclusion of Tensor Cores in consumer GPUs. It also demonstrates the value of NVIDIA's AI expertise in consumer markets.

DLSS has become a competitive advantage for NVIDIA. AMD and Intel have introduced their own upscaling technologies, but DLSS generally delivers better quality and performance. This advantage comes from NVIDIA's expertise in AI and the maturity of its software stack.

## Reflex and G-SYNC: latency and display technologies

Beyond rendering performance, NVIDIA has invested in reducing the latency between a player's input and the resulting action on screen. NVIDIA Reflex, introduced in 2020, optimizes the rendering pipeline to reduce system latency by improving how the CPU and GPU coordinate their work. In a traditional rendering pipeline, the CPU submits render work to the GPU asynchronously, which can create a queue of frames that adds tens of milliseconds of delay between mouse click and visual response. Reflex dynamically reduces this queue, keeping the CPU and GPU in tighter synchronization. The result is measurable reductions in system latency, typically 20 to 50 percent, depending on the game and hardware configuration. Reflex has been adopted by major esports titles including Valorant, Fortnite, Apex Legends, and Counter-Strike 2, where millisecond differences in input responsiveness affect competitive outcomes.

G-SYNC, NVIDIA's variable refresh rate technology, addresses a different display problem: screen tearing and stuttering caused by mismatched frame delivery rates. Traditional monitors refresh at fixed intervals, typically 60 or 144 times per second. If the GPU delivers a new frame in the middle of a refresh cycle, the monitor displays part of the old frame and part of the new frame, creating a visible tear. G-SYNC allows the monitor to synchronize its refresh to the GPU's frame delivery, eliminating tearing without the input lag introduced by traditional VSync. G-SYNC Ultimate adds HDR support with full-array local dimming and 1000-nit brightness. G-SYNC Compatible, a software-based mode, validates FreeSync monitors for use with NVIDIA GPUs, extending the technology's reach to displays that lack dedicated G-SYNC hardware.

## Automotive and edge platforms: DRIVE and Jetson

NVIDIA's expansion beyond traditional computing markets includes automotive and robotics platforms. The DRIVE platform targets autonomous vehicles. The Jetson platform targets robotics and edge AI. Both are growth vectors for NVIDIA, although they remain smaller than the core data center and gaming businesses.

The DRIVE AGX platform provides in-vehicle computing for autonomous driving. DRIVE Orin offers up to 254 TOPS (trillions of operations per second) for autonomous driving workloads. DRIVE Orin is a system-on-chip that integrates ARM CPU cores, NVIDIA GPU cores, and dedicated hardware for vision and sensor processing.

DRIVE Thor is the next-generation platform, announced for 2025. It unifies cluster, infotainment, automated driving, and parking functions in a single centralized computer. This consolidation reduces cost and complexity for automotive manufacturers. Instead of separate electronic control units for each function, a single Thor computer handles everything.

Driveworks is the operating system for driverless cars. It provides the software framework for autonomous driving applications, including sensor fusion, perception, planning, and control. Driveworks supports multiple sensor types including cameras, lidar, radar, and ultrasonic sensors.

The automotive business is characterized by long development cycles. A vehicle platform may take five years to develop, and the software stack evolves continuously. NVIDIA's strategy is to provide a scalable platform that can be updated over the life of the vehicle. DRIVE Thor is designed to be over-the-air upgradable, allowing manufacturers to add features and improve performance after the vehicle is sold.

The Jetson platform targets embedded and edge AI. Jetson Orin is the current generation, with multiple SKUs for different performance and power requirements. The Jetson AGX Orin delivers up to 275 TOPS with 15 to 60 watts of power consumption. The Jetson Orin NX offers up to 100 TOPS with 10 to 25 watts. The Jetson Orin Nano provides up to 40 TOPS with 7 to 15 watts, starting at $199.

Jetson modules are complete computers on a module. They include ARM CPUs, NVIDIA GPUs, memory, storage, and networking. They are designed to be integrated into custom hardware. Robots, drones, industrial equipment, and edge AI appliances all use Jetson modules. The lower-power variants can run on battery power, enabling mobile robots.

The Jetson Thor series, announced as the next-generation robotics platform, extends the Jetson architecture for humanoid robotics. Robotics is emerging as a significant AI application, with humanoid robots requiring substantial computing power for perception, planning, and control. Jetson Thor is optimized for these workloads.

The Isaac robotics platform provides the software infrastructure that makes Jetson hardware productive for robotics developers. Isaac Sim is a physics-based robotics simulation environment that runs on NVIDIA GPUs, allowing engineers to test robot behaviors in photorealistic virtual environments before deploying to physical hardware. Simulation is essential for robotics because real-world testing is slow, expensive, and potentially dangerous. Isaac Sim can simulate thousands of scenarios in parallel, training and validating perception and control systems at a pace that would be impossible with physical robots alone. The simulation environment uses NVIDIA's Omniverse technology for rendering and physics, providing accurate sensor simulation for cameras, lidar, and radar.

Isaac Lab, built on top of Isaac Sim, is a framework specifically designed for training robot policies using reinforcement learning. It provides reference environments for common robot morphologies, including manipulators, quadrupeds, and humanoids, along with tools for defining reward functions and curriculum strategies. Researchers can train a robot to walk, grasp objects, or navigate complex environments entirely in simulation, then transfer the learned policy to a physical robot with minimal fine-tuning.

Isaac ROS provides a set of ROS 2 (Robot Operating System) packages optimized for NVIDIA hardware. ROS is the de facto standard middleware for robotics, handling inter-process communication, hardware abstraction, and package management. Isaac ROS accelerates common robotics tasks like visual odometry, depth perception, object detection, and stereo disparity by offloading them to GPU-accelerated CUDA libraries. A robot built with Isaac ROS on Jetson hardware can process sensor data faster and with lower latency than one relying on CPU-based ROS nodes.

Isaac GR00T is NVIDIA's generalist robotics foundation model, designed specifically for humanoid robots. Announced at GTC 2024, GR00T takes language, video, and demonstration inputs and generates robot actions. The model is trained on data from multiple robot platforms and simulation environments, giving it a broad understanding of physical interactions. GR00T represents NVIDIA's bet that the same foundation model approach that transformed language and vision will transform robotics, reducing the need for per-task engineering and enabling robots to generalize across situations they were not explicitly trained for.

OSMO (Orchestration and Scale for Microservices) ties the Isaac ecosystem together by managing the AI workflows that robotics development requires. Training a robot policy involves simulation, data generation, model training, and deployment, each of which may run on different hardware. OSMO coordinates these stages, scheduling compute resources across GPUs and managing the data pipeline between simulation output and model training input. For organizations deploying robots at scale, OSMO reduces the operational complexity of keeping the training and deployment pipeline running.

The Jetson lineage itself illustrates how far edge AI has come. The original Jetson TX2, launched in 2017, delivered 1.3 TFLOPS of compute. The Jetson Nano, released in 2019 at $99, brought GPU-accelerated AI to hobbyists and educators with 0.5 TFLOPS in a 5-to-10-watt power envelope. The Jetson AGX Xavier pushed performance to 32 TOPS, and the Xavier NX variant delivered 21 TOPS in a smaller form factor. The current Jetson Orin generation tops out at 275 TOPS with the AGX Orin, a more than 200-fold improvement over the TX2 in fewer than eight years. Each generation extended what was possible at the edge: TX2 enabled basic object detection, Orin enables real-time multi-sensor perception for autonomous machines.

The robotics platform connects directly to NVIDIA's broader AI factory vision. The same GPUs that train large language models also train robotics foundation models. The same networking infrastructure that connects GPUs in a data center also connects simulated robots in a training cluster. NVIDIA's thesis is that robotics will follow the same scaling pattern as language models: larger models trained on more data using more compute, with the resulting capabilities commoditized through foundation models like GR00T. If this thesis is correct, NVIDIA sells the compute for every stage: simulation on data center GPUs, training on H100s and Blackwells, and inference on Jetson at the edge.

The IGX platform provides advanced functional safety and security for edge AI. Industrial applications require certification for safety-critical operations. IGX includes hardware and software features that facilitate certification for medical, industrial, and automotive applications where failures could cause injury.

Automotive and robotics are strategically important because they represent diversification beyond the core data center and gaming markets. AI training will eventually saturate. AI inference will continue to grow, but competition may increase. Automotive and robotics provide additional growth vectors that leverage NVIDIA's AI expertise but address different market segments.

## The annual architecture cadence as competitive weapon

NVIDIA's commitment to an annual architecture cadence is a key competitive advantage. Each year, NVIDIA releases a new GPU architecture with performance improvements and new features. This cadence is aggressive for a semiconductor company, where 18 to 24 month cycles are more typical.

The annual cadence puts competitive pressure on AMD, Intel, and other rivals. Each year that NVIDIA releases a new architecture and competitors do not, NVIDIA's performance lead increases. Each year that competitors try to match NVIDIA's previous generation, NVIDIA releases a new architecture that resets the competition.

The cadence also sends a signal to customers. If they buy NVIDIA GPUs, they know that better GPUs will be available next year. If they wait, they can get more performance. But waiting also means delaying their AI projects, which has its own cost. Most customers choose to buy now and upgrade later. This creates a continuous upgrade cycle that benefits NVIDIA's revenue.

Maintaining the annual cadence requires substantial R&D investment. Each architecture costs hundreds of millions of dollars to develop, spanning design, verification, testing, and software support. The mask set for a leading-edge GPU costs approximately $500 million. This is a barrier to entry. A startup or smaller company cannot afford to match NVIDIA's cadence.

The annual cadence is not just about hardware. It requires coordination across software, libraries, and developer tools. Each new architecture must be supported in CUDA, cuDNN, TensorRT, and the entire CUDA-X library collection. Frameworks like TensorFlow and PyTorch must be optimized for the new architecture.

## Manufacturing and supply chain: the TSMC dependence

NVIDIA is a fabless semiconductor company, which means it designs chips but does not manufacture them. Manufacturing is outsourced to TSMC (Taiwan Semiconductor Manufacturing Company), the world's leading contract semiconductor manufacturer. TSMC manufactures NVIDIA's most advanced GPUs on its 3nm and 5nm process nodes.

This reliance on TSMC is both a strength and a risk. The strength is that TSMC has the world's most advanced manufacturing capabilities. No other company can match TSMC's yield, performance, and capacity at the leading edge. NVIDIA's GPUs benefit from this manufacturing excellence.

The risk is concentration. NVIDIA is dependent on a single supplier for its most critical manufacturing. If TSMC cannot meet demand, or if geopolitical tensions disrupt operations, NVIDIA has no alternative. The Taiwan Strait is a geopolitical flashpoint, and any conflict could disrupt semiconductor manufacturing.

HBM (high-bandwidth memory) is another critical component. HBM is stacked memory that sits on the same package as the GPU, connected through a wide, high-speed interface. SK hynix, Micron, and Samsung supply HBM. The supply of HBM has been a constraint at times, limiting GPU production.

The supply chain for high-end GPUs has unusual security considerations. An H100 GPU can sell for $30,000 or more on the secondary market. A tray of GPUs is worth millions of dollars. NVIDIA ships GPUs via armored car to data centers. The security in transit is commensurate with the value of the components.

Export controls add complexity to the supply chain. Starting in 2022, the US government restricted the export of advanced AI chips to China. This included the A100 and H100 GPUs. NVIDIA developed modified versions, the A800 and H20, which complied with export controls by reducing some capabilities. These modified chips could be exported to China but offered lower performance.

## Conclusion: from graphics to AI infrastructure

The transformation of NVIDIA from a consumer graphics company to an AI infrastructure provider is reflected in its product portfolio and architecture evolution. The early architectures, Tesla through Pascal, were designed primarily for graphics with compute capabilities added. The later architectures, Volta through Blackwell, are designed primarily for AI with graphics capabilities maintained.

The product lines have shifted similarly. In 2016, gaming represented approximately 50% to 60% of NVIDIA's revenue. By 2026, the Data Center segment represented 90% of revenue. Gaming, professional visualization, automotive, and other segments combined represented just 10%. This shift occurred in less than a decade, a remarkably rapid transformation for a large company.

The architectural innovations that enabled this transformation were Tensor Cores, which specialized GPUs for AI workloads, and the software stack, which made GPUs accessible to AI developers. CUDA, cuDNN, TensorRT, and the broader CUDA-X ecosystem created a platform that made NVIDIA GPUs the default choice for AI development.

From the GeForce 256, the first GPU, to the GB200, the engine of AI reasoning, NVIDIA's architecture evolution has been consistent. Each generation delivers more performance, more features, and more capabilities. The investments in CUDA, in Tensor Cores, in networking, and in software have created an integrated stack that competitors struggle to match. The company that was thirty days from bankruptcy in 1997 now produces the most critical computing infrastructure for the AI revolution.
