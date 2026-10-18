# Chapter 7: Who Buys the Shovels

NVIDIA's transformation from a gaming graphics company to the foundational infrastructure provider for the AI revolution is reflected in its customer base. The company that once sold GeForce cards to gamers now sells H100 and Blackwell GPUs to the world's most valuable companies. The customer roster includes every major hyperscaler, leading AI research labs, Fortune 500 enterprises, automotive OEMs, healthcare systems, and sovereign nations. This chapter maps the NVIDIA customer ecosystem, analyzing who buys, why they buy, and how their purchasing patterns shape NVIDIA's business.

The customer data tells a clear story. NVIDIA's Data Center revenue reached 193.7 billion dollars in fiscal year 2026, up 68 percent year-over-year. This revenue is highly concentrated. A small number of hyperscalers reportedly account for 40 to 50 percent of total Data Center revenue. The top five customers, likely Microsoft, Meta, Google, Amazon, and Oracle, represent the majority of NVIDIA's highest-margin products. This concentration is both a strength and a vulnerability. It provides scale and predictability, but it creates dependency risk as these customers develop their own alternatives.

## The Hyperscalers: Primary Customers and Potential Competitors

The hyperscalers are NVIDIA's largest, most important, and most dangerous customer segment. Microsoft, Google, Amazon, Meta, and Oracle collectively represent the majority of NVIDIA's Data Center revenue. These companies have multiyear, multigenerational partnerships with NVIDIA. They also have the engineering resources and financial scale to develop custom accelerators that could reduce their dependence on NVIDIA. Understanding their purchasing patterns is essential to understanding NVIDIA's business.

### Microsoft: The OpenAI Partner

Microsoft's relationship with NVIDIA is intertwined with its partnership with OpenAI. The two relationships form a strategic triangle: Microsoft Azure hosts OpenAI's GPT models on NVIDIA systems, while also building its own AI infrastructure using NVIDIA GPUs. This triangular relationship creates both stability and complexity for NVIDIA.

#### The OpenAI connection

The OpenAI partnership is foundational to Microsoft's AI strategy. Microsoft invested approximately 13 billion dollars in OpenAI beginning in 2023, giving Microsoft an exclusive partnership on OpenAI technologies and preferred access to OpenAI's models. Azure is the exclusive cloud provider for OpenAI, meaning that ChatGPT, GPT-4, and subsequent models run on Microsoft infrastructure.

This arrangement creates enormous demand for NVIDIA GPUs. Training GPT-4 required thousands of H100 GPUs running for months. The inference infrastructure serving ChatGPT to hundreds of millions of users requires even more GPUs. Every time a user queries ChatGPT, that query processes on an NVIDIA GPU hosted in a Microsoft Azure data center.

The scale of this deployment is staggering. OpenAI has been among the largest purchasers of NVIDIA GPUs globally. The training runs for GPT-4 and subsequent models represent some of the largest computing projects in history. Microsoft's infrastructure build-out to support OpenAI has cost tens of billions of dollars, with NVIDIA as the primary hardware vendor.

#### Azure AI infrastructure

Beyond OpenAI, Microsoft Azure offers AI infrastructure services to external customers. Azure OpenAI Service allows enterprises to access GPT models through APIs. Azure Machine Learning provides a platform for building and deploying custom AI models. All of these services depend on NVIDIA infrastructure.

Microsoft has committed to deploying Vera Rubin-based instances among the first wave of cloud providers. This commitment demonstrates the strategic importance of NVIDIA to Azure's competitiveness. Being first to offer the latest GPU technology is a differentiator in the cloud market, where performance differences of 20-30 percent can determine which provider wins large AI workloads.

The partnership spans multiple domains: AI infrastructure, cloud services, and physical AI initiatives. Microsoft and NVIDIA are collaborating on industrial digital twins through Microsoft's partnership with NVIDIA on Omniverse. The companies are integrating NVIDIA AI Enterprise with Azure to provide enterprise-grade AI software and support.

#### The Maia accelerator question

Microsoft developed the Maia 100 accelerator as a custom AI chip for internal workloads. Announced in 2023, Maia represents Microsoft's effort to reduce dependence on NVIDIA for certain workloads. The chip powers Microsoft's own AI services, including Copilot offerings and Bing Chat.

The strategic question is how Maia will affect NVIDIA purchasing. The evidence suggests a hybrid approach: Maia for known internal workloads, NVIDIA for frontier AI and external customer services. Maia is used internally for Microsoft's AI services, but Azure customers seeking top-tier performance still use NVIDIA-based instances.

This pattern reflects a broader trend among hyperscalers. Custom silicon targets stable, well-understood workloads where the requirements are predictable. NVIDIA GPUs remain essential for cutting-edge training and experimental workloads where performance matters more than cost optimization.

Microsoft's AI infrastructure spending exceeds 10 billion dollars annually as of 2025. Even if Maia captures a portion of this spending, NVIDIA's share likely remains in the billions annually. The relationship is symbiotic: Microsoft needs NVIDIA's latest GPUs for competitive AI services, while NVIDIA benefits from Azure's massive scale and OpenAI partnership.

#### Purchase scale and patterns

Microsoft's NVIDIA purchasing is measured in billions of dollars annually. The company has committed to multiyear, multigenerational GPU deployments. This commitment provides NVIDIA with revenue visibility and allows for capacity planning with manufacturing partners.

The purchase pattern includes H100 and H200 GPUs for current deployments, Blackwell GPUs for next-generation infrastructure, and commitments to purchase Rubin-based systems when available. Microsoft's infrastructure build-out is multi-generational, locking in demand for years.

The strategic importance of this relationship cannot be overstated. Microsoft is one of the world's largest companies by market capitalization, with nearly 100 billion dollars in annual revenue. Its AI infrastructure spending represents a significant portion of NVIDIA's revenue. Losing Microsoft as a customer would be material. Maintaining the relationship requires NVIDIA to keep Microsoft satisfied with pricing, allocation, and technology roadmaps.

### Meta: The Multi-generational Commitment

Meta represents perhaps NVIDIA's most important hyperscaler relationship. In November 2024, the companies announced a multiyear, multigenerational strategic partnership. The scope is breathtaking: Meta will deploy NVIDIA CPUs, networking, and millions of Blackwell and Rubin GPUs across on-premises, cloud, and AI infrastructure. The partnership covers multiple GPU generations, locking in demand for years.

#### The Llama training imperative

Meta's partnership with NVIDIA is driven by its AI research ambitions. The company trains massive models like Llama, which reached 405 billion parameters in 2024. It runs AI inference across Facebook, Instagram, WhatsApp, and emerging products like AI glasses and Ray-Ban Meta smart glasses. The computational requirements are enormous.

Training Llama 3 405B required thousands of GPUs running for months. The training cost exceeded 100 million dollars in compute alone. Inference for Meta's AI features across billions of users requires even more infrastructure. Every AI-generated sticker, every AI-powered recommendation, every AI assistant feature depends on GPU compute.

By partnering deeply with NVIDIA, Meta ensures priority access to the latest GPU technology. In a supply-constrained market where H100 GPUs were in short supply, having a strategic partnership guaranteed allocation. This allocation advantage is strategically significant because AI capabilities have become competitive differentiators for Meta's products.

#### On-premises deployment strategy

Unlike some hyperscalers that primarily use cloud-based GPUs, Meta deploys NVIDIA infrastructure both on-premises and in the cloud. The company operates its own AI research facilities with custom-built GPU clusters. This on-premises deployment requires purchasing GPUs directly rather than accessing them through cloud services, which creates direct revenue for NVIDIA.

Meta's on-premises strategy reflects several factors: data privacy concerns for training on user data, cost optimization from owning rather than renting infrastructure, and the need for custom hardware configurations optimized for Meta's specific workloads. By deploying NVIDIA infrastructure on-premises, Meta gains control over its AI destiny while depending on NVIDIA for the core hardware.

#### MTIA and the coexistence model

Meta developed the Meta Training and Inference Accelerator (MTIA) as a custom silicon solution. MTIA targets recommendation systems and inference workloads, particularly for Facebook and Instagram's content ranking algorithms. These workloads are stable, well-understood, and don't require cutting-edge GPU performance.

Meta has publicly stated that MTIA will not replace NVIDIA for cutting-edge training. This explicit statement validates NVIDIA's continued relevance even to customers developing custom accelerators. The division of labor is clear: custom silicon for internal, stable workloads, NVIDIA for frontier AI research and experimental work.

This coexistence model is becoming standard across hyperscalers. Rather than choosing between custom silicon and NVIDIA GPUs, companies are using both. Custom silicon handles 30-40% of workloads where requirements are predictable. NVIDIA GPUs handle 60-70% of workloads where performance matters more than cost.

#### Strategic partnership details

The November 2024 partnership announcement included several specific commitments:

**Millions of GPUs:** Meta will purchase millions of Blackwell and Rubin GPUs over multiple years. The precise dollar value was not disclosed, but the commitment likely exceeds 10 billion dollars based on typical GPU pricing and the scale of "millions" of units.

**CPUs and networking:** Meta will also purchase NVIDIA Grace CPUs and networking products. This full-stack approach demonstrates the value of the Mellanox acquisition. By selling CPUs, networking, and GPUs as an integrated solution, NVIDIA increases its attach rate per deployment.

**On-premises, cloud, and edge:** The partnership spans deployment models from on-premises data centers to cloud services to edge computing. This breadth reflects Meta's diverse infrastructure needs across its product portfolio.

**AI research collaboration:** Beyond hardware purchasing, Meta and NVIDIA are collaborating on AI research. This includes work on transformer architectures, efficiency improvements, and AI safety. Research collaboration strengthens the relationship and creates shared technical understanding.

From NVIDIA's perspective, the Meta partnership represents the ideal customer relationship: multi-generational commitment, large scale, and public validation that NVIDIA GPUs remain essential even as customers develop custom alternatives. The partnership also creates a competitive moat because switching from NVIDIA would require renegotiating a strategic relationship, not just changing hardware suppliers.

### Google Cloud: The TPU Coexistence

Google presents an interesting case study in the coexistence of custom silicon and NVIDIA GPUs. The company has been developing TPUs (Tensor Processing Units) since 2016 and uses them extensively for internal workloads. Google Search, Gmail, YouTube, and Google Bard all run on TPUs. The TPU v5 and v5p generations are competitive with NVIDIA H100 for specific workloads. Despite this internal TPU investment, Google Cloud remains a major NVIDIA customer.

#### TPU architecture and positioning

Google's TPU is a custom accelerator designed specifically for tensor operations, which are the mathematical operations at the heart of deep learning. Unlike NVIDIA's GPUs, which are general-purpose parallel processors, TPUs are specialized for machine learning. This specialization allows TPUs to be highly efficient for Google's specific workload patterns.

TPU development has progressed through multiple generations: TPU v1, v2, v3, v4, and v5/v5p. Each generation improved performance, memory bandwidth, and interconnect technology. The TPU v5 Pod, which connects thousands of TPUs with high-speed interconnects, can train large language models competitively with NVIDIA-based clusters.

Google uses TPUs internally for its core products. Google Search ranking models train and run on TPUs. YouTube recommendation algorithms use TPUs. Gmail's spam filtering and Smart Reply features depend on TPUs. Google Bard and subsequent AI models train on TPU Pods. This internal use creates a massive installed base of TPUs that provides economies of scale.

#### Why Google Cloud needs NVIDIA

Despite its TPU investment, Google Cloud remains a major NVIDIA customer for several reasons:

**External customer demand:** Google Cloud customers want general-purpose GPUs for their diverse AI workloads. TPUs are optimized for Google's specific workload patterns but may not be optimal for every customer. Customers who have developed code on CUDA or who need compatibility with existing infrastructure often prefer NVIDIA GPUs.

**Portability requirements:** Many enterprises want workload portability across cloud providers. NVIDIA GPUs are available on every major cloud platform. TPUs are only available on Google Cloud. Customers who want multi-cloud flexibility prefer standard GPUs that work everywhere.

**Performance leadership:** For cutting-edge training workloads, NVIDIA's latest GPUs often outperform TPUs. Training the largest models requires the absolute best performance available. Google Cloud offers both TPUs and NVIDIA GPUs, allowing customers to choose based on their specific needs.

**Software ecosystem:** CUDA has a much larger developer ecosystem than Google's TPU software stack. Customers who have invested in CUDA code and expertise prefer NVIDIA infrastructure. Rewriting code for TPUs creates switching costs that discourage adoption.

#### Partnership scope

Google Cloud is among the first cloud providers to deploy Vera Rubin-based instances. This commitment demonstrates Google's continued investment in NVIDIA infrastructure despite its TPU capabilities. Being first to offer Rubin GPUs is a competitive differentiator for Google Cloud in the cloud market.

The partnership includes DGX Cloud collaboration. DGX Cloud is NVIDIA's managed AI supercomputer service offered through cloud providers. Google Cloud hosts DGX Cloud infrastructure, providing customers with turnkey access to NVIDIA-optimized AI supercomputers. This service simplifies AI infrastructure deployment for enterprises.

Integration with Google AI services creates another connection point. Google Cloud's Vertex AI platform supports NVIDIA GPUs. TensorFlow and JAX, popular machine learning frameworks, are optimized for both TPUs and NVIDIA GPUs. This co-optimization allows customers to choose the hardware that best fits their needs without changing their software stack.

#### Competitive dynamics

The Google relationship demonstrates that custom silicon and NVIDIA GPUs can coexist within the same customer. The division of labor is becoming clear: TPUs for Google's internal, stable workloads, NVIDIA GPUs for cloud customers and experimental work.

This coexistence model benefits NVIDIA. Rather than losing Google entirely to TPUs, NVIDIA retains the portion of Google's business that values general-purpose GPUs. The cloud customer segment, which continues to grow, provides a reliable revenue stream even as Google's internal TPU deployment expands.

The risk is that TPUs improve to the point where they match NVIDIA GPUs for general workloads. If TPUs become clearly superior for most use cases, Google Cloud could shift more aggressively toward TPUs and away from NVIDIA. However, the CUDA ecosystem moat makes this difficult. The millions of developers trained on CUDA and the billions of lines of CUDA code create a switching cost that protects NVIDIA's position even as TPUs improve.

### Amazon Web Services: The Cost Optimizer

AWS has perhaps the most aggressive custom silicon strategy among hyperscalers. Trainium for training and Inferentia for inference represent Amazon's effort to reduce NVIDIA dependence. Trainium 2, announced at re:Invent 2024, targets 2025 deployment. The chips are tightly integrated with AWS ecosystem, offering lower cost than NVIDIA for specific workloads. Yet AWS remains a major NVIDIA customer, demonstrating that even the most aggressive in-house silicon efforts cannot fully displace NVIDIA.

#### Trainium and Inferentia strategy

Amazon's custom silicon approach targets both training and inference workloads:

**Inferentia:** Launched in 2019, Inferentia is an inference accelerator designed to run trained machine learning models efficiently in production. Inferentia offers low latency and low cost for inference workloads like image recognition, speech recognition, and recommendation systems. AWS offers Inferentia-based instances (Inf1) that are significantly cheaper than GPU-based instances for inference.

**Trainium:** Announced in 2020 and deployed in 2023, Trainium targets training workloads. Trainium accelerators are designed specifically for deep learning training, offering performance competitive with NVIDIA GPUs for certain workloads at lower cost. Trainium is tightly integrated with AWS's machine learning ecosystem, including SageMaker for model development and deployment.

**Trainium 2:** Announced at re:Invent 2024, Trainium 2 represents a significant performance improvement. The chip targets 2025 deployment and promises to be competitive with NVIDIA's H100 for specific workloads. Trainium 2 demonstrates Amazon's commitment to custom silicon despite the massive investment required.

The strategic rationale for Trainium and Inferentia is cost optimization. AWS operates on thin margins relative to other Amazon businesses. Reducing the cost of infrastructure through custom silicon improves AWS profitability. Custom chips also give AWS control over its technology stack, reducing dependence on external suppliers.

#### Why AWS still needs NVIDIA

Despite its custom silicon investments, AWS remains a major NVIDIA customer for several reasons:

**Performance leadership:** For cutting-edge training workloads, NVIDIA's GPUs still outperform Trainium. Training the largest language models requires the absolute best performance available. AWS customers training frontier models use NVIDIA-based instances (P4, P5) because they deliver better performance than Trainium.

**Software ecosystem:** CUDA has broader software support than AWS's custom chips. Customers who have existing CUDA codebases prefer NVIDIA instances to avoid rewriting code. The CUDA ecosystem moat protects NVIDIA even against AWS's cost-optimized alternatives.

**Market differentiation:** AWS must offer the best infrastructure to remain competitive in the cloud market. If Google Cloud and Microsoft Azure offer NVIDIA's latest GPUs and AWS only offers Trainium, AWS would lose customers who demand top-tier performance. Offering both Trainium and NVIDIA GPUs allows AWS to serve all customer segments.

**AI services:** AWS's own AI services, including those available through Bedrock, depend on NVIDIA infrastructure for cutting-edge models. Bedrock offers access to models from Anthropic, Stability AI, and other AI companies. Many of these models train and run on NVIDIA infrastructure, creating dependency.

#### Partnership evolution

The expanded AWS partnership announced in Q4 fiscal 2026 includes new technology integrations across interconnect technology, cloud infrastructure, open models, and physical AI. Amazon is deploying Vera Rubin-based instances among the first wave of cloud providers. This continued commitment demonstrates that custom silicon and NVIDIA GPUs will coexist within AWS.

The AWS strategy is tiered: Trainium and Inferentia for price-sensitive workloads, NVIDIA for performance-sensitive workloads. This tiered approach allows AWS to optimize costs where possible while still offering top-tier performance for customers who need it.

From NVIDIA's perspective, AWS represents both a customer and a competitor. AWS is a major customer that spends billions on NVIDIA GPUs annually. But AWS is also developing custom chips that reduce NVIDIA's addressable market within AWS. The relationship requires NVIDIA to maintain technology leadership to justify premium pricing, while also accepting that some portion of AWS workloads will shift to Trainium and Inferentia.

#### Financial implications

The financial impact of AWS's custom silicon strategy is significant but manageable. Trainium and Inferentia may capture 30-40% of AWS AI workloads over time. However, NVIDIA retains 60-70% of workloads, particularly the high-margin training segment where performance matters most. The revenue that NVIDIA loses to custom chips is partially offset by the growth in overall AI infrastructure spending. As AWS's total AI infrastructure spending grows, NVIDIA's absolute revenue from AWS may continue to increase even if its market share within AWS declines.

The key risk is that Trainium improves to the point where it matches NVIDIA GPUs for most workloads. If that occurs, AWS could shift more aggressively to Trainium and away from NVIDIA. However, the CUDA ecosystem creates switching costs that protect NVIDIA's position. AWS customers who have invested in CUDA infrastructure will be reluctant to switch to Trainium unless the performance or cost advantage is substantial.

### Oracle Cloud Infrastructure: The Pure-Play Partner

Oracle represents the purest hyperscaler partnership model. The company has no significant custom silicon effort. Instead, Oracle Cloud Infrastructure is all-in on NVIDIA. OCI is among the first to deploy Vera Rubin-based instances. The company has strategic collaboration for AI workloads and participates in DGX Cloud partnerships. Oracle's strategy is differentiation through rapid deployment of latest NVIDIA technology.

#### Oracle's AI infrastructure strategy

Oracle's cloud strategy differs from larger hyperscalers. AWS, Google Cloud, and Microsoft Azure each have massive scale and compete broadly across cloud services. Oracle Cloud Infrastructure focuses on specific segments: Oracle database workloads, enterprise applications, and now AI infrastructure.

The AI infrastructure strategy is straightforward: offer the latest NVIDIA GPUs as quickly as possible. Oracle was among the first to offer H100 GPUs. Oracle was among the first to announce H200 GPUs. Oracle is among the first to commit to Rubin-based instances. This speed to market creates differentiation. Customers who want cutting-edge AI infrastructure without the complexity of hyperscaler-specific silicon find Oracle attractive.

Oracle's ZFS storage and Exadata database systems create synergies with AI infrastructure. Many AI workloads require high-performance storage and databases. Oracle's ability to offer integrated solutions (compute, storage, networking, database) reduces complexity for enterprise customers.

#### Strategic partnership details

The Oracle-NVIDIA partnership includes several components:

**DGX Cloud:** Oracle hosts DGX Cloud infrastructure alongside other cloud providers. DGX Cloud provides turnkey AI supercomputers that NVIDIA manages. Oracle's participation gives customers another cloud option for DGX Cloud and increases NVIDIA's total addressable market.

**Rapid deployment:** Oracle commits to deploying new GPU generations quickly. Being first or among the first to offer Rubin-based instances gives Oracle a competitive advantage. This speed requires close coordination between Oracle and NVIDIA on testing, validation, and deployment processes.

**AI enterprise software:** Oracle integrates NVIDIA AI Enterprise software with its cloud services. NVIDIA AI Enterprise provides enterprise-grade support, security, and API compatibility for NVIDIA's AI software stack. The integration makes Oracle's cloud more attractive to enterprise customers who require enterprise software certifications.

**Industry-specific solutions:** Oracle and NVIDIA collaborate on industry-specific AI solutions for healthcare, financial services, and manufacturing. Oracle's deep expertise in these verticals, combined with NVIDIA's AI infrastructure, creates differentiated offerings.

#### Financial implications

From NVIDIA's perspective, Oracle is an ideal customer. The company has no custom silicon efforts that could displace NVIDIA GPUs. Oracle's total dependence on NVIDIA creates a stable customer relationship. While Oracle is smaller than AWS, Google Cloud, or Microsoft Azure, its focused strategy makes it an important partner.

The risk is that Oracle remains a smaller cloud provider relative to larger hyperscalers. OCI's market share in cloud computing is in the single digits, far below AWS, Microsoft Azure, and Google Cloud. This limits Oracle's total purchasing power relative to larger competitors.

However, Oracle's focused strategy means that NVIDIA's share of Oracle's AI infrastructure spending is near 100%. Every dollar Oracle spends on AI infrastructure likely goes to NVIDIA. This concentration within Oracle makes the relationship strategically important even if Oracle's total spend is less than larger hyperscalers.

#### Partnership value

The Oracle partnership also creates optionality for NVIDIA. Having a cloud partner that is all-in on NVIDIA provides leverage in negotiations with other hyperscalers. If Microsoft Azure, Google Cloud, or AWS become too aggressive with custom silicon, NVIDIA can point to Oracle as an alternative that offers pure NVIDIA infrastructure without conflicts of interest.

The partnership also validates NVIDIA's technology leadership. Oracle's choice to go all-in on NVIDIA rather than develop custom silicon is a vote of confidence in NVIDIA's long-term competitiveness. This validation influences other potential customers who are deciding between NVIDIA and alternatives.

### The Hyperscaler Risk Assessment

The hyperscaler customer segment presents both opportunity and risk. The opportunity is scale. These customers purchase tens of thousands of GPUs annually, generating billions in revenue. Their AI capex continues to accelerate, driving NVIDIA growth. Multi-generational partnerships create visibility and predictability.

The risk is vertical integration. All major hyperscalers except Oracle are developing custom accelerators. The question is not whether they will reduce NVIDIA purchasing, but by how much. The current pattern suggests a hybrid future rather than total displacement.

#### The hybrid model

The hybrid model emerging across hyperscalers looks like this:

**30-40% custom silicon share:** Custom accelerators like Google TPU, AWS Trainium, Microsoft Maia, and Meta MTIA will capture stable, well-understood workloads. These include recommendation systems, content ranking, inference for production models, and internal AI services. The requirements for these workloads are predictable, allowing custom silicon to be optimized effectively.

**60-70% NVIDIA share:** NVIDIA GPUs will retain cutting-edge training workloads, experimental research, frontier model development, and external customer services. These workloads require the absolute best performance and benefit from CUDA's software ecosystem. The higher value of these workloads means NVIDIA retains the premium segment.

This outcome is manageable for NVIDIA. While market share declines from near-total dominance to 60-70%, the absolute dollar value may continue to grow because total AI infrastructure spending is increasing rapidly. NVIDIA sells fewer GPUs but at higher prices and margins. The installed base becomes more focused on frontier AI where NVIDIA's advantages are greatest.

#### Demand timing risk

Beyond the structural shift to custom silicon, hyperscalers present demand timing risk. AI infrastructure spending by hyperscalers is volatile and depends on multiple factors:

**Economic conditions:** In economic downturns, hyperscalers may reduce capex even for strategic initiatives like AI. While AI is considered critical, spending moderation is possible if economic conditions deteriorate significantly.

**ROI realization:** Hyperscalers are investing tens of billions in AI infrastructure. If AI services fail to generate expected revenue, they may moderate spending. Microsoft's Copilot monetization, Google's AI-powered search, and Meta's AI features all need to generate sufficient return to justify continued heavy investment.

**Technology cycles:** Hyperscaler capex has historically been cyclical. Periods of heavy investment alternate with periods of digesting previous investments. The current AI boom may eventually enter a digestion phase where spending moderates.

**Competitive dynamics:** Hyperscalers may reduce spending if competitors pull back. If one hyperscaler moderates AI capex, others may follow to avoid over-investing relative to competitors.

These demand timing risks create volatility and uncertainty. NVIDIA's revenue is highly concentrated among a small number of customers whose spending decisions are outside NVIDIA's control. A moderation by even one or two hyperscalers would materially impact NVIDIA's revenue growth.

#### Strategic mitigation

NVIDIA is not passive in the face of these risks. The company has several strategies to mitigate hyperscaler dependency:

**Enterprise diversification:** NVIDIA is aggressively pursuing enterprise AI adoption. Fortune 500 companies building AI infrastructure create a new customer segment beyond hyperscalers. As enterprises grow from 10% to 20% to 30% of NVIDIA's revenue, hyperscaler concentration declines.

**Sovereign AI:** Nations building domestic AI infrastructure represent another diversification path. Sovereign AI projects in countries like Japan, India, France, and Saudi Arabia create government-scale customers independent of hyperscalers.

**Vertical markets:** Automotive, healthcare, financial services, and manufacturing each represent specialized AI infrastructure markets. While smaller than hyperscalers individually, collectively they provide diversification.

**Systems integration:** By selling complete systems (DGX, HGX, NVL72) rather than individual GPUs, NVIDIA creates switching costs. Once a customer has invested in NVIDIA-certified systems, changing architectures requires replacing entire infrastructure, not just swapping GPUs.

**Software attach:** NVIDIA AI Enterprise software creates recurring revenue and switching costs. Customers who have standardized on NVIDIA's software stack are less likely to switch to alternative hardware.

The most likely outcome is gradual diversification rather than sudden disruption. Hyperscalers will remain the largest customer segment but will reduce their relative share as enterprises, sovereign AI projects, and vertical markets grow. Custom silicon will capture some workloads but NVIDIA will retain the cutting-edge training segment where margins are highest. This outcome represents risk but not existential threat.

## AI Native Companies: The Frontier Model Builders

The AI native companies represent NVIDIA's most strategically important customer segment after hyperscalers. These companies, including OpenAI, Anthropic, xAI, and others, are building the frontier AI models that define the state of the art. Their computational requirements are enormous and growing. Their purchasing decisions shape which models become competitive and which companies lead in AI capabilities.

### OpenAI: The ChatGPT Infrastructure

OpenAI's relationship with NVIDIA is foundational to the generative AI boom. ChatGPT, which launched in November 2022 and triggered the current AI wave, runs entirely on NVIDIA infrastructure. The historical partnership dates back to GPT-3 and earlier models. OpenAI has been among the largest purchasers of NVIDIA GPUs for AI research.

#### Training infrastructure scale

Training GPT-4 required an enormous compute infrastructure. While exact specifications were not disclosed, industry analysis suggests that training GPT-4 required thousands of GPUs running for several months. The compute cost exceeded 100 million dollars, primarily for GPU time and electricity. This training run was one of the largest computing projects in history.

The infrastructure required includes not just GPUs but also:

**High-speed networking:** NVIDIA's InfiniBand networking products connect thousands of GPUs into a single cluster. The training speed depends on how quickly GPUs can communicate with each other. Slow networking bottlenecks training, so NVIDIA's full-stack approach (GPUs plus networking) is essential.

**Storage systems:** Training large models requires accessing enormous datasets. High-performance storage systems that can feed data to GPUs fast enough to avoid idle time are critical. NVIDIA works with storage partners to provide optimized solutions.

**Software stack:** CUDA, NVIDIA Collective Communications Library (NCCL), and other software components optimize training efficiency. OpenAI has worked closely with NVIDIA to optimize training code for NVIDIA hardware.

#### Inference infrastructure

Inference infrastructure serving ChatGPT to hundreds of millions of users requires even more GPUs than training. Each ChatGPT query requires matrix operations that consume GPU compute. With over 100 million weekly active users, the cumulative inference demand is enormous.

OpenAI operates multiple inference clusters distributed globally to provide low-latency responses. These clusters run 24/7, consuming substantial electricity and requiring continuous maintenance. The inference infrastructure cost likely exceeds the training cost within months of deployment.

NVIDIA's inference optimization technologies, including TensorRT and transformer engines, help OpenAI reduce inference costs. These optimizations increase the number of queries that a single GPU can handle, improving economics. The H100 GPU with its transformer engine optimizations is particularly efficient for transformer models like GPT.

#### Partnership dynamics

The OpenAI-NVIDIA partnership is symbiotic but complex. OpenAI needs NVIDIA's latest GPUs for competitive model training. Each new GPT version requires more compute than the previous one. GPT-5 will likely require an order of magnitude more training compute than GPT-4. This creates ongoing demand for NVIDIA's most powerful GPUs.

NVIDIA benefits from OpenAI's success. Every ChatGPT announcement reinforces NVIDIA's position as the standard for AI development. When users marvel at ChatGPT's capabilities, they are indirectly seeing NVIDIA's technology in action. OpenAI's success drives demand for AI infrastructure, which benefits NVIDIA.

However, the relationship adds complexity through Microsoft's involvement. Microsoft is both OpenAI's exclusive cloud provider and a major NVIDIA customer. Microsoft's 13 billion dollar investment in OpenAI creates a triangular relationship. Microsoft provides Azure infrastructure that runs NVIDIA GPUs to host OpenAI models. This arrangement benefits both NVIDIA (through Azure GPU purchases) and OpenAI (through Azure infrastructure and Microsoft capital).

#### Strategic importance

OpenAI is strategically important to NVIDIA for several reasons:

**Technology leadership:** OpenAI defines the state of the art in AI capabilities. GPT-4 set benchmarks that competitors race to match. By powering OpenAI, NVIDIA powers the frontier of AI. This leadership position reinforces NVIDIA's brand and technology credibility.

**Competitive signaling:** Other AI companies observe OpenAI's infrastructure choices. If OpenAI uses NVIDIA GPUs exclusively, this signals that NVIDIA is the standard for frontier AI research. This influences other companies' infrastructure decisions.

**Product feedback:** OpenAI's extreme use cases provide feedback that helps NVIDIA improve its products. The challenges of training trillion-parameter models at scale push NVIDIA's technology forward. Solutions developed for OpenAI benefit all customers.

**Revenue scale:** OpenAI's infrastructure spending reaches into the billions of dollars annually. As OpenAI scales ChatGPT and develops new models, its compute requirements continue growing. This provides NVIDIA with a growing revenue stream.

### Anthropic: The Claude Partnership

NVIDIA announced a strategic partnership with Anthropic that combines investment and deep technology collaboration. Anthropic scales its Claude model on Microsoft Azure using NVIDIA systems. The multi-generational infrastructure commitment ensures Anthropic has access to cutting-edge GPUs for model development.

#### Constitutional AI differentiation

Anthropic's focus on constitutional AI and AI safety differentiates it from competitors. The company's research on AI alignment, interpretability, and safety mechanisms requires specialized infrastructure. Claude's constitutional AI approach, which involves explicit constraints on model behavior, demands additional compute for constraint enforcement during training and inference.

NVIDIA's partnership with Anthropic is strategically important because it positions NVIDIA as a supporter of responsible AI development. As AI safety concerns grow from governments, researchers, and the public, being associated with safety-focused companies like Anthropic provides reputational benefits.

#### Infrastructure requirements

Anthropic's Claude models rival GPT-4 in capability and thus require comparable infrastructure. Training Claude 3 (and subsequent versions) required thousands of GPUs running for months. Inference infrastructure serving Claude through APIs and partnerships (including with Amazon and Google) requires substantial GPU deployment.

Anthropic has raised billions of dollars from investors including Amazon, Google, and Spark Capital. Much of this capital funds GPU purchases from NVIDIA. As Anthropic scales its models and expands its API business, its infrastructure requirements continue growing.

#### Partnership value

For NVIDIA, the Anthropic partnership provides several benefits:

**Competitive positioning:** Anthropic is a major competitor to OpenAI. By partnering with Anthropic, NVIDIA ensures that it powers the leading alternative to ChatGPT. This reduces dependence on any single AI company and provides market diversification.

**Safety credibility:** Anthropic's focus on AI safety aligns with NVIDIA's stated commitment to responsible AI development. The partnership enhances NVIDIA's credibility with policymakers, researchers, and the public who are concerned about AI safety.

**Cloud diversification:** While Anthropic uses Microsoft Azure for some infrastructure, it also partners with Amazon Web Services and Google Cloud. This multi-cloud approach creates NVIDIA GPU demand across multiple cloud providers rather than concentrating on one.

### xAI: Elon Musk's AI Infrastructure

xAI, founded by Elon Musk in 2023, operates one of the world's largest GPU supercomputers. The company's rapid infrastructure buildout demonstrates the pace of AI company capex. xAI went from announcement to operating a massive AI supercomputer in under two years.

#### The Memphis supercomputer

xAI's primary AI supercomputer, located in Memphis, Tennessee, contains over 100,000 GPUs (a mix of H100 and other NVIDIA products). This makes it one of the largest AI supercomputers in existence. The supercomputer was built in record time, demonstrating the urgency of AI infrastructure competition.

The scale of xAI's infrastructure is staggering. 100,000 GPUs at roughly 30,000 dollars each represents a 3 billion dollar hardware investment, not counting networking, cooling, power, and facility costs. The electricity consumption rivals that of small cities. This is the scale required to train frontier AI models in 2024-2026.

#### The Grok model

xAI's Grok model competes directly with ChatGPT, Claude, and other leading AI assistants. Grok training required compute on the same scale as GPT-4 and Claude. Each new version of Grok requires more compute than the previous one, driving ongoing infrastructure investment.

xAI's competitive positioning is distinctive. Grok is integrated with X (formerly Twitter), giving it access to real-time data and a distribution channel to hundreds of millions of users. This integration creates advantages but also requires substantial inference infrastructure to serve X's user base.

#### Strategic dynamics

Elon Musk's involvement creates unique dynamics. Musk co-founded OpenAI before leaving due to strategic disagreements. He has been critical of OpenAI's transition from nonprofit to for-profit and its partnership with Microsoft. His founding of xAI represents direct competition with his former company.

For NVIDIA, xAI represents both opportunity and complexity. The opportunity is enormous infrastructure spending. xAI has raised billions of dollars and invested heavily in NVIDIA GPUs. The complexity is that Musk has criticized NVIDIA's pricing and has suggested he may develop alternative infrastructure. However, given NVIDIA's technology leadership, xAI remains dependent on NVIDIA GPUs for the foreseeable future.

### Inference Providers: The Cost Optimization Layer

A new category of AI company has emerged focused on efficient inference. Baseten, DeepInfra, Fireworks AI, and Together AI are leading inference providers achieving significant cost reductions using NVIDIA Blackwell. NVIDIA revealed that these providers are achieving 10x cost reduction with open-source models on Blackwell. This cost efficiency is critical for making AI services economically viable at scale.

#### The inference economics challenge

Inference represents a growing portion of AI compute spend. While training gets more attention because it requires enormous upfront investment, inference costs accumulate over time. ChatGPT serves hundreds of millions of users, each query requiring inference compute. The cumulative inference cost often exceeds the training cost within months of deployment.

The economics challenge is that inference must be extremely cost-efficient to be profitable. Users are unwilling to pay substantial amounts per query. Advertising and subscription revenue must cover both infrastructure costs and profit margins. Reducing inference cost per query is therefore critical.

#### Blackwell efficiency improvements

NVIDIA's Blackwell architecture delivers not just training performance but inference efficiency. The 10x cost reduction that inference providers are achieving comes from several Blackwell improvements:

**Higher performance per dollar:** Blackwell GPUs process more tokens per dollar than previous generations. This reduces the number of GPUs required for a given inference workload.

**Transformer engine optimizations:** Blackwell's transformer engine is specifically optimized for transformer models, which power most large language models. Specialized hardware for transformer operations improves efficiency.

**Memory bandwidth:** Blackwell's high memory bandwidth allows faster loading of model weights, reducing latency and improving throughput. More memory allows larger batch sizes, which improves GPU utilization.

**Power efficiency:** Blackwell delivers better performance per watt, reducing electricity costs. Electricity is a major component of inference operating expenses.

#### Strategic implications

The success of inference providers validates NVIDIA's value proposition beyond training. Blackwell delivers not just training performance but inference efficiency. The 10x cost reduction demonstrates that NVIDIA's latest architecture delivers economic benefits across the AI stack.

As AI services move from research to production, inference becomes an increasingly large portion of total compute spend. NVIDIA's ability to serve this market with cost-efficient solutions is strategically important. The inference providers are pioneers in production AI deployment, and their success with Blackwell will influence other companies' infrastructure decisions.

## Enterprise AI Adoption: The Fortune 500 Wave

The most significant growth opportunity for NVIDIA beyond hyperscalers is enterprise AI adoption. CEO Jensen Huang stated in Q4 fiscal 2026: "Enterprise adoption of agents is skyrocketing. Our customers are racing to invest in AI compute." The evidence suggests this trend is accelerating across Fortune 500 companies.

### AI Factory Construction

Enterprises are building AI factories for large-scale model training and inference. These facilities range from a few hundred GPUs for mid-sized companies to tens of thousands of GPUs for large enterprises. The pattern is consistent: companies start with pilot projects, see value, and then scale to full AI infrastructure deployment. This creates a multi-year purchasing cycle as enterprises move from experimentation to production.

#### The AI factory concept

The AI factory concept, popularized by NVIDIA, refers to infrastructure specifically designed for AI workloads. Unlike traditional data centers that run diverse applications, AI factories are optimized for the unique requirements of AI training and inference:

**Dense compute:** AI factories pack GPUs more densely than traditional data centers. The power and cooling requirements are much higher because GPUs consume more power and generate more heat than CPUs.

**High-speed networking:** AI training requires GPUs to communicate constantly. Traditional networking is insufficient. AI factories use NVIDIA's InfiniBand or specialized Ethernet to provide the bandwidth and latency required for distributed training.

**Specialized storage:** AI workloads require storage that can deliver data fast enough to keep GPUs fed. Parallel file systems and high-throughput storage are essential.

**Software stack:** AI factories include NVIDIA AI Enterprise software, which provides enterprise-grade support, security, and API compatibility. The software layer makes the infrastructure accessible to enterprise IT teams.

#### Enterprise deployment patterns

Enterprise AI adoption follows a consistent pattern:

**Pilot phase:** Companies start with small pilot projects using cloud-based GPU instances or on-premises GPU clusters. These pilots might involve a few dozen GPUs. The goal is to prove value and build internal expertise.

**Production phase:** Successful pilots scale to production deployments. This involves hundreds or thousands of GPUs. Companies build dedicated AI infrastructure rather than borrowing from existing data centers.

**Expansion phase:** Production deployments expand as use cases multiply. What starts with one or two AI applications grows to dozens. The AI infrastructure expands accordingly, reaching thousands of GPUs for large enterprises.

This multi-year adoption pattern creates a predictable revenue stream for NVIDIA. Enterprise AI adoption is in its early stages, so the runway for growth is long. As more enterprises move from pilot to production to expansion, NVIDIA's enterprise revenue will grow.

### India Systems Integrators: The Global Channel

NVIDIA announced that India's global systems integrators are building enterprise AI agents. Infosys, Persistent Systems, Tech Mahindra, and Wipro are all developing AI agent infrastructure using NVIDIA platforms. These partnerships represent a significant channel into global enterprise markets. Companies that outsource IT and AI development to Indian firms will increasingly encounter NVIDIA-based solutions.

#### The systems integrator model

Systems integrators (SIs) are IT services companies that help enterprises plan, implement, and manage technology projects. Indian SIs including Infosys, Wipro, Tech Mahindra, and HCL Technologies are among the world's largest, with hundreds of thousands of employees and operations across dozens of countries.

Enterprises hire SIs for AI projects because they lack internal AI expertise. Rather than building in-house AI teams, enterprises contract with SIs who provide the necessary skills and experience. The SIs then recommend and implement AI infrastructure, often based on their standard technology platforms.

#### NVIDIA's SI partnerships

NVIDIA's partnerships with Indian SIs create a channel into global enterprise markets:

**Infosys:** Infosys Topaz is an AI-first set of services using NVIDIA platforms. Infosys has trained thousands of employees on NVIDIA AI technologies. The partnership gives NVIDIA access to Infosys's global client base, which includes many Fortune 500 companies.

**Wipro:** Wipro's ai360 platform leverages NVIDIA AI infrastructure. Wiper has developed industry-specific AI solutions for banking, healthcare, and manufacturing using NVIDIA GPUs. These solutions can be deployed across Wipro's client base.

**Tech Mahindra:** Tech Mahindra's AI partnerships with NVIDIA focus on telecommunications and manufacturing. The company develops AI solutions for 5G network optimization, factory automation, and other specialized use cases.

**Persistent Systems:** Persistent builds enterprise AI agents using NVIDIA platforms. The company focuses on banking, insurance, and healthcare, where it has deep domain expertise.

The SI strategy is about scale. A single partnership with Infosys or Wipro gives NVIDIA access to thousands of enterprise customers worldwide. These Indian IT giants have deep relationships with Fortune 500 companies across industries. Their adoption of NVIDIA platforms creates a gravitational pull that brings enterprises into the NVIDIA ecosystem.

#### Economic implications

The SI partnerships have significant economic implications for NVIDIA:

**Market reach:** Rather than selling to each enterprise individually, NVIDIA can sell through SIs who already have relationships with thousands of enterprises. This dramatically increases NVIDIA's sales reach and efficiency.

**Standardization:** SIs tend to standardize on specific technology stacks to reduce complexity. Once an SI standardizes on NVIDIA platforms, all of their projects will use NVIDIA infrastructure, creating recurring revenue.

**Training and certification:** NVIDIA trains SI employees on CUDA, AI development, and infrastructure management. These trained employees become NVIDIA advocates within their client organizations, creating demand pull.

**Global footprint:** Indian SIs have operations worldwide, giving NVIDIA global reach beyond the United States. As AI adoption accelerates in Europe, Asia, and other regions, NVIDIA is positioned through SI partnerships to capture this growth.

### Industrial Software Partnerships

NVIDIA has partnered with global industrial software leaders to target manufacturing, engineering, and industrial design workflows. Siemens, Cadence, and Synopsys have all expanded strategic partnerships with NVIDIA. These companies are co-developing industrial AI operating systems and accelerating engineering and design workflows.

#### Siemens partnership

The Siemens partnership is particularly significant. The companies are developing industrial AI for manufacturing, digital twins, and factory automation. This targets the massive industrial sector, which represents trillions in economic value.

The partnership includes several components:

**Industrial digital twins:** Siemens and NVIDIA are integrating Siemens' Xcelerator platform with NVIDIA's Omniverse. Industrial digital twins allow manufacturers to simulate factories, production lines, and products in virtual environments before building physical versions. This reduces costs and accelerates development.

**Factory automation:** AI-powered factory automation uses computer vision and machine learning to optimize manufacturing processes. NVIDIA's Metropolis vision AI platform combined with Siemens' industrial automation creates solutions for quality control, predictive maintenance, and production optimization.

**Generative design:** AI can generate optimized designs for products and components. NVIDIA's generative AI capabilities combined with Siemens' CAD software enable engineers to explore design possibilities that would be impossible to discover manually.

Industrial AI applications often require real-time processing, edge deployment, and integration with operational technology. NVIDIA's full-stack approach, including the Omniverse platform for digital twins and Jetson platform for edge AI, is well-suited to these requirements.

#### Cadence and Synopsys partnerships

Cadence and Synopsys are the two largest electronic design automation (EDA) software companies. Their tools are used to design chips, printed circuit boards, and electronic systems. Both companies have expanded strategic partnerships with NVIDIA to accelerate engineering and design workflows.

The partnerships focus on GPU acceleration for EDA workloads. Chip design involves enormous computational requirements. Simulating chip behavior, verifying correctness, and optimizing performance are computationally intensive tasks. By accelerating these workloads on NVIDIA GPUs, Cadence and Synopsys can dramatically reduce design time.

This creates a virtuous cycle. NVIDIA uses Cadence and Synopsys tools to design its own GPUs. The partnership improves these tools by adding GPU acceleration. Better tools enable NVIDIA to design better GPUs, which in turn provide more acceleration for the tools. This symbiotic relationship strengthens NVIDIA's position in the semiconductor ecosystem.

### Financial Services and Healthcare

Financial services and healthcare represent two high-value verticals for enterprise AI. These industries have the capital to invest in AI infrastructure and clear use cases where AI can provide substantial value.

#### Financial services AI

Financial services firms use AI for numerous applications:

**Fraud detection:** Machine learning models analyze transaction patterns to identify fraudulent activity in real time. These models require low-latency inference to approve or decline transactions quickly.

**Algorithmic trading:** AI models predict market movements and execute trades automatically. Trading firms invest heavily in compute infrastructure to gain millisecond advantages in trading speed.

**Risk assessment:** Banks use AI to assess creditworthiness and loan risk. These models analyze borrower data to predict default probability and set appropriate interest rates.

**Customer service:** Chatbots and virtual assistants handle customer inquiries, reducing the need for human agents. These AI assistants require natural language processing capabilities powered by GPU inference.

Financial services firms have particular requirements that NVIDIA's infrastructure addresses:

**Low latency:** Trading and fraud detection require decisions in milliseconds. NVIDIA's GPUs provide the computational performance for real-time inference.

**Regulatory compliance:** Financial services are heavily regulated. NVIDIA AI Enterprise software includes security features and compliance certifications that financial firms require.

**Reliability:** Financial systems cannot fail. NVIDIA's enterprise-grade support and hardware quality meet financial firms' reliability requirements.

#### Healthcare AI

Healthcare applications include medical imaging, drug discovery, and clinical decision support:

**Medical imaging:** AI models analyze X-rays, MRIs, CT scans, and other medical images to detect diseases. These models require sophisticated computer vision capabilities powered by GPUs. NVIDIA's Clara AGX platform is specifically designed for medical devices and imaging.

**Drug discovery:** AI can predict how molecules will interact with proteins, dramatically accelerating drug discovery. This is computationally intensive work that benefits from GPU acceleration. NVIDIA's BioNeMo platform targets AI-driven biology and drug discovery.

**Clinical decision support:** AI models assist doctors by analyzing patient data and suggesting diagnoses or treatments. These models must be accurate and reliable, requiring robust infrastructure.

Healthcare has particular requirements:

**Regulatory approval:** Medical AI systems require regulatory approval (FDA clearance in the United States). NVIDIA works with healthcare companies to ensure its infrastructure meets regulatory requirements.

**Data privacy:** Healthcare data is protected by regulations like HIPAA in the United States. NVIDIA's infrastructure includes security features that help healthcare companies maintain compliance.

**Accuracy:** Medical AI systems must be extremely accurate. Errors can have life-or-death consequences. NVIDIA's reliable, high-performance infrastructure helps healthcare companies deploy accurate AI models.

#### Eli Lilly partnership

The Eli Lilly partnership exemplifies healthcare AI adoption. The companies co-innovated an AI lab to reinvent drug discovery in the age of AI. The platform expansion announced in Q4 fiscal 2026 supports lab-in-the-loop workflows, accelerating GPU-accelerated biology and drug discovery breakthroughs.

Drug discovery is a compelling AI use case because the value of discovering a new drug can justify enormous compute investment. A single successful drug can generate billions in revenue. The computational cost of AI-accelerated drug discovery, while substantial, is small compared to the potential payoff.

The partnership focuses on several areas:

**Protein structure prediction:** AI models can predict how proteins fold, which is critical for understanding biology and designing drugs. These models require enormous computational resources.

**Molecule generation:** AI can generate new molecules with desired properties. This expands the chemical space that drug researchers can explore.

**Clinical trial optimization:** AI can help design better clinical trials and analyze results more quickly. This accelerates the drug development timeline.

The Eli Lilly partnership demonstrates how NVIDIA's technology can create value in even the most specialized industries. Drug discovery was not traditionally a GPU-intensive application, but AI is transforming it into one. NVIDIA's ability to serve these specialized, high-value applications creates a moat that competitors focused on general-purpose computing cannot easily replicate.

## Automotive and Robotics: The Physical AI Frontier

NVIDIA's automotive business reached 604 million dollars in Q4 fiscal 2026, up 2 percent quarter-over-quarter and 6 percent year-over-year. Full-year automotive revenue was 2.3 billion dollars, up 39 percent year-over-year. This growth is driven by adoption of NVIDIA self-driving platforms. But automotive is just one component of NVIDIA's physical AI strategy, which extends to robotics, industrial automation, and autonomous machines.

### Mercedes-Benz: Production Deployment

The partnership with Mercedes-Benz on the all-new CLA class represents a significant milestone. The enhanced Level 2 driver assistance system is powered by NVIDIA DRIVE AV software. This is not a research project or a concept car. It is a production vehicle shipping with NVIDIA technology. The distinction matters because revenue from production vehicles is recurring and scalable. Each CLA sold generates revenue for NVIDIA through the automotive supply chain.

#### DRIVE AV software

NVIDIA DRIVE AV is NVIDIA's autonomous vehicle software stack. It includes perception (using cameras, radar, and lidar to understand the environment), localization (determining the vehicle's position), planning (deciding how to navigate), and control (executing driving commands). The software runs on NVIDIA DRIVE Orin and upcoming Thor automotive SoCs (systems on chips).

The Mercedes CLA deployment uses DRIVE AV for Level 2 driver assistance. Level 2 means the vehicle can control steering and acceleration under certain conditions, but the driver must remain engaged and ready to take over. This is the same level as Tesla's Autopilot and many other driver assistance systems.

#### Strategic significance

The Mercedes deployment is strategically significant for several reasons:

**Production validation:** Moving from research partnerships to production deployment proves that NVIDIA's automotive technology works in real-world conditions. Automotive is a highly regulated industry with strict safety requirements. Achieving production deployment validates NVIDIA's technology and processes.

**Revenue scaling:** Each Mercedes CLA sold generates revenue for NVIDIA. While the per-vehicle revenue is small relative to GPU sales, automotive volumes are large. If Mercedes deploys NVIDIA technology across multiple vehicle lines, the revenue becomes substantial.

**OEM credibility:** Mercedes is one of the most prestigious automotive brands. Its choice of NVIDIA technology influences other OEMs. If Mercedes trusts NVIDIA for driver assistance, other automakers are more likely to follow.

**Technical partnership:** The Mercedes partnership goes beyond licensing. The companies are co-developing next-generation autonomous driving capabilities. This creates a long-term relationship that extends beyond individual vehicle models.

### The DRIVE Hyperion Ecosystem

NVIDIA's automotive strategy extends beyond OEMs to include the entire automotive supply chain. DRIVE Hyperion is NVIDIA's reference platform for autonomous vehicles, combining compute, sensors, and software. The ecosystem approach creates switching costs for OEMs. Once an automaker standardizes on DRIVE Hyperion, changing suppliers requires requalifying the entire sensor and compute stack.

#### Tier 1 suppliers

NVIDIA has partnered with major Tier 1 automotive suppliers who build components for OEMs:

**Magna:** One of the largest automotive suppliers, Magna manufactures vehicles and components for numerous OEMs. Magna's partnership with NVIDIA involves integrating DRIVE technology into Magna's systems.

**ZF Group:** A German supplier specializing in driveline and chassis technology, ZF Group partners with NVIDIA to integrate autonomous driving capabilities into its products.

**Bosch:** The world's largest automotive supplier, Bosch develops components for virtually every major automaker. Bosch's partnership with NVIDIA covers sensors, computers, and software for autonomous driving.

**Astrom (formerly Honda-Keihin):** This joint venture between Honda and Keihin develops automotive electronics. Its partnership with NVIDIA focuses on autonomous driving systems.

These Tier 1 supplier partnerships create reach across the automotive industry. Magna, ZF, Bosch, and Astrom sell to dozens of OEMs worldwide. By partnering with these suppliers, NVIDIA ensures its technology is available throughout the automotive ecosystem.

#### Sensor partners

DRIVE Hyperion includes sensors as well as compute. NVIDIA has partnered with sensor manufacturers to provide a complete autonomous driving stack:

**Aeva:** Aeva develops frequency-modulated continuous wave (FMCW) lidar, which offers advantages over traditional lidar for autonomous driving. Aeva's sensors are integrated into DRIVE Hyperion.

**Hesai:** A Chinese lidar manufacturer, Hesai provides sensors for autonomous vehicles and robotics. Hesai's partnership with NVIDIA ensures sensor compatibility with NVIDIA's compute platforms.

**Omnivision:** A leading image sensor company, Omnivision provides cameras for automotive applications. Its sensors are used in DRIVE Hyperion for computer vision.

**Sony:** Sony is a major image sensor supplier for automotive cameras. Its partnership with NVIDIA ensures sensor compatibility and optimization for NVIDIA's computer vision algorithms.

**Quanta:** A Taiwanese manufacturer, Quanta produces cameras and other components for autonomous vehicles. Its partnership with NVIDIA involves manufacturing sensors for DRIVE Hyperion.

This sensor ecosystem creates a complete solution that OEMs can adopt rather than assembling components from multiple vendors. The integrated approach reduces complexity and ensures all components work together seamlessly.

### Robotics and Physical AI

Robotics represents an emerging growth opportunity for NVIDIA. The company has announced partnerships with Boston Dynamics, Caterpillar, Franka Robotics, Humanoid, LG Electronics, and NEURA Robotics. The NVIDIA robotics stack includes Isaac for robot simulation and control, and the new Cosmos and Isaac GR00T open models for physical AI.

#### Physical AI requirements

Physical AI for robotics has different requirements than data center AI:

**Real-time processing:** Robots must process sensor data and make decisions in real time. Latency of more than a few milliseconds can cause robots to fail or behave dangerously. NVIDIA's GPUs provide the computational performance for real-time inference.

**Edge deployment:** Robots often operate without reliable connectivity to the cloud. AI models must run on-board the robot rather than in cloud data centers. NVIDIA's Jetson platform provides edge AI capabilities in a compact, low-power form factor.

**Sensor fusion:** Robots combine data from multiple sensors: cameras, lidar, radar, tactile sensors, and more. Fusing this data requires computational power and sophisticated algorithms. NVIDIA's platforms are optimized for sensor fusion workloads.

**Precise control:** Robots must execute precise movements. This requires control algorithms running at high frequency. NVIDIA's hardware provides deterministic performance needed for control loops.

#### Isaac platform

NVIDIA Isaac is a robotics platform that includes:

**Isaac Sim:** A simulation environment for training robots in virtual environments before deploying them in the real world. Simulation dramatically reduces the cost and time of robot development. Robots can learn in simulation where mistakes don't damage physical hardware.

**Isaac Perceptor:** A perception package for robots that includes pre-trained models for object detection, pose estimation, and scene understanding. These models help robots understand their environment.

**Isaac Manipulator:** A package for robotic arms that includes motion planning, grasp planning, and control algorithms. This simplifies programming robot arms for manipulation tasks.

**Isaac GR00T:** A foundation model for humanoid robots that enables more general-purpose robot capabilities. GR00T can understand natural language instructions and translate them into robot actions.

#### Partner deployments

NVIDIA's robotics partnerships demonstrate diverse applications:

**Boston Dynamics:** The company famous for the Spot robot and Atlas humanoid uses NVIDIA Isaac for robot simulation and control. Boston Dynamics is exploring AI-driven capabilities for its robots.

**Caterpillar:** The construction equipment company is using NVIDIA platforms for autonomous construction equipment. Autonomous excavators, bulldozers, and trucks can operate continuously without human operators, improving productivity and safety.

**Franka Robotics:** A German company specializing in robotic arms, Franka uses NVIDIA's platforms for precise manipulation. Franka's robots are used in manufacturing, research, and healthcare.

**Humanoid:** A startup developing humanoid robots, Humanoid uses NVIDIA Isaac for simulation and control. Humanoid robots require sophisticated AI to navigate human environments and manipulate objects designed for human hands.

**LG Electronics:** The Korean electronics company uses NVIDIA platforms for service robots, industrial robots, and autonomous mobility. LG's diverse robotics portfolio benefits from NVIDIA's unified platform.

**NEURA Robotics:** A German robotics company, NEURA develops cognitive robots that can work alongside humans. The company uses NVIDIA's platforms for perception, planning, and control.

The robotics opportunity is distinct from autonomous vehicles. While autonomous vehicles are a specific type of robot, general-purpose robotics has much broader applicability. Industrial robots, warehouse robots, service robots, medical robots, and construction robots all represent potential markets. NVIDIA's platform approach allows it to serve all of these segments with a common technology stack.

## Sovereign AI: Nations as Customers

Sovereign AI represents a new customer category: nations building domestic AI infrastructure. The concept is that countries want AI infrastructure within their borders to maintain data sovereignty and develop domestic AI capabilities. These national-scale AI projects are funded by governments and often involve partnerships with local technology companies.

### The Sovereign AI Thesis

The sovereign AI thesis is straightforward. AI is becoming critical infrastructure for national competitiveness. Countries want control over their AI destiny rather than depending on foreign cloud providers. They want data to remain within national borders for security and regulatory reasons. They want domestic AI capabilities for economic development and national security.

Several factors drive sovereign AI initiatives:

**Data localization:** Regulations like GDPR in Europe and similar laws in other countries require certain data to remain within national borders. AI systems processing this data must be hosted domestically.

**National security:** AI has military and intelligence applications. Countries want domestic AI capabilities rather than depending on potential adversaries. The United States restricts AI chip exports to China precisely because AI has national security implications.

**Economic competitiveness:** AI is expected to drive economic growth in coming decades. Countries want domestic AI industries to capture economic value rather than importing AI services from foreign companies.

**Cultural and linguistic preservation:** AI models trained primarily on English data from the United States may not serve other countries well. Countries want to train models on their own languages and cultural contexts.

**Regulatory compliance:** Different countries have different AI regulations. The EU's AI Act classifies AI systems by risk and imposes requirements on high-risk applications. Companies want AI infrastructure that complies with local regulations.

NVIDIA is uniquely positioned to serve sovereign AI projects. The company has the technology stack, the neutral positioning (not American, Chinese, or European in the way that hyperscalers are), and the scale to deploy national AI infrastructure. Sovereign AI projects often involve building AI supercomputers, training national language models, and developing AI applications for government services. These are multi-year, multi-billion dollar initiatives.

### India: The Strategic Growth Market

India represents one of the most important sovereign AI opportunities. The country has a large technology workforce, a growing AI startup ecosystem, and government support for digital infrastructure. India's large English-speaking population and democratic institutions make it a natural partner for Western AI companies.

#### Digital public infrastructure

India has developed world-class digital public infrastructure including Aadhaar (biometric identity system), UPI (digital payments), and CoWIN (vaccination tracking). This digital infrastructure provides a foundation for AI applications. AI can enhance these systems by improving fraud detection, personalization, and service delivery.

India's government has announced AI initiatives including:

**Bhashini:** A National Language Translation Mission to develop AI translation between India's many languages. This requires training models on Indian languages and deploying inference infrastructure.

**AI for Agriculture:** Using AI to improve crop yields, reduce pesticide use, and optimize water usage. These applications require AI infrastructure in rural areas or cloud connectivity to agricultural regions.

**Healthcare AI:** Diagnostic AI for rural clinics, drug discovery for diseases prevalent in India, and epidemiological modeling. These applications require both training infrastructure and edge deployment.

#### NVIDIA's India partnerships

NVIDIA's partnerships with Indian systems integrators (Infosys, Wipro, Tech Mahindra, Persistent) provide a channel into the Indian market. These companies are building AI solutions for government and enterprise customers using NVIDIA infrastructure.

Beyond SIs, NVIDIA has direct partnerships with Indian companies and institutions:

**Reliance Industries:** The conglomerate led by Mukesh Ambani is building AI infrastructure in India. Reliance's Jio platform has access to hundreds of millions of Indians and is developing AI-powered services.

**Tata Consultancy Services:** India's largest IT services company, TCS partners with NVIDIA on AI solutions. TCS serves global clients but also works on Indian government projects.

**Indian Institutes of Technology:** The IITs are India's premier engineering schools. NVIDIA partners with IITs on research and education, providing GPU infrastructure and curriculum support.

The opportunity in India is enormous. India has over 1.4 billion people and a growing economy. If India achieves its economic potential, AI infrastructure spending will reach tens of billions annually. NVIDIA's early positioning in India provides a first-mover advantage.

### Japan: Government-Industry Collaboration

Japan has a history of government-industry collaboration in technology. The country's success in electronics and automotive manufacturing involved coordination between government, industry, and academia. Japan is applying a similar approach to AI.

#### National AI computing centers

Japan has established national AI computing centers that provide shared infrastructure for researchers and companies. These centers use NVIDIA GPUs and are funded through government-industry partnerships. The centers serve multiple purposes: advancing AI research, supporting AI startups, and training the workforce.

Japanese companies including Toyota, Sony, and Fujitsu are investing in AI. Toyota, as a major automotive company, needs AI for autonomous driving. Sony, as an electronics and entertainment company, needs AI for products and services. Fujitsu, as an IT services company, needs AI for its offerings.

#### Strategic positioning

Japan's geopolitical position makes sovereign AI particularly important. Japan is a U.S. ally but also has significant economic ties with China. Japan wants to maintain technological independence while navigating great power competition. Developing domestic AI capabilities serves both economic and strategic interests.

NVIDIA's partnerships with Japanese companies and institutions give the company access to this market. Japanese customers have historically been loyal to suppliers who demonstrate long-term commitment. NVIDIA's years of investment in Japan create relationships that competitors cannot quickly replicate.

### Europe: Digital Sovereignty

Europe's focus on digital sovereignty and regulation-compliant AI infrastructure aligns with NVIDIA's ability to deploy within specific regulatory frameworks. The EU's AI Act creates requirements for AI systems that NVIDIA's infrastructure can help companies meet.

#### Regulatory compliance

The EU AI Act classifies AI systems by risk: unacceptable risk (banned), high risk (heavily regulated), limited risk (transparency requirements), and minimal risk (unregulated). High-risk applications including critical infrastructure, medical devices, and employment decisions require conformity assessments and risk management.

NVIDIA's infrastructure helps companies comply with these regulations through:

**Traceability:** NVIDIA's tools can track model training data and decisions, providing the audit trails required by regulations.

**Explainability:** Some of NVIDIA's software tools help explain model decisions, addressing transparency requirements.

**Security:** NVIDIA AI Enterprise includes security features that help protect models and data, addressing safety requirements.

#### Sovereign AI initiatives

European countries including France, Germany, and the Nordic countries have announced sovereign AI initiatives:

**France:** France has committed 1.5 billion euros to AI research and infrastructure. The French government is working with NVIDIA and other companies to build AI supercomputers. France's Mistral AI is a leading European AI company that trains models on NVIDIA infrastructure.

**Germany:** Germany's AI strategy focuses on industrial applications. German companies including Siemens, Bosch, and SAP are investing in AI. NVIDIA's partnerships with these companies create a channel into the German market.

**Nordics:** Sweden, Norway, Denmark, and Finland have strong AI research ecosystems. These countries are building AI infrastructure and have successful AI startups. NVIDIA's partnerships with Nordic companies provide access to this market.

Europe's regulatory focus creates both challenges and opportunities for NVIDIA. Regulations increase compliance costs, but they also create barriers for competitors who cannot meet regulatory requirements. NVIDIA's scale and resources allow it to navigate European regulations more easily than smaller competitors.

### The Middle East and NEOM

Gulf region countries, including Saudi Arabia with its NEOM project and the United Arab Emirates, have announced massive AI infrastructure investments. These projects combine smart city development, AI research, and economic diversification beyond oil. The capital commitments are enormous. NEOM alone involves hundreds of billions in investment. NVIDIA is positioned to provide the AI infrastructure for these projects.

#### NEOM project

NEOM is a planned city in northwestern Saudi Arabia that will be powered by AI and renewable energy. The city is designed as a testbed for technologies including autonomous mobility, flying taxis, and automated infrastructure. NEOM's development requires enormous AI infrastructure for planning, construction, and eventual operation.

NVIDIA is providing AI infrastructure for NEOM's development and operation. This includes:

**Digital twins:** Before building physical infrastructure, NEOM uses digital twins to simulate and optimize designs. NVIDIA's Omniverse platform powers these simulations.

**Autonomous systems:** NEOM plans to use autonomous vehicles, drones, and robots throughout the city. These systems require AI infrastructure for training and operation.

**Smart city management:** AI will optimize energy, water, transportation, and other city services. This requires AI inference infrastructure deployed throughout the city.

#### UAE AI initiatives

The United Arab Emirates has established the world's first Ministry of Artificial Intelligence and has invested heavily in AI capabilities. Abu Dhabi's Technology Innovation Institute developed the Falcon open-source language models, which train on NVIDIA infrastructure. The UAE is building AI supercomputers to support its AI ambitions.

The Gulf region's financial resources allow for rapid AI infrastructure deployment. While the populations are small, the per-capita investment in AI is enormous. This creates a concentrated market for NVIDIA's highest-end products.

## OEM and Server Partners: The Channel to Market

NVIDIA does not sell most GPUs directly to end customers. The company sells through OEM partners including Dell Technologies, Hewlett Packard Enterprise, Lenovo, and Supermicro. These server vendors build and sell NVIDIA-certified systems validated for AI workloads. The OEM channel is critical to NVIDIA's go-to-market strategy.

### NVIDIA-Certified Systems Program

The NVIDIA-Certified Systems program validates servers from major OEMs for performance, functionality, scalability, and security. For enterprise customers, certification reduces the risk of purchasing AI infrastructure. Rather than sourcing components and assembling systems, customers can buy certified systems with confidence that they will work for AI workloads.

#### Certification process

The certification process involves extensive testing:

**Performance testing:** Systems are tested to ensure they deliver the expected GPU performance. This includes verifying GPU connectivity, memory bandwidth, and computational throughput.

**Functionality testing:** Systems are tested with actual AI workloads to ensure they work correctly. This includes testing training and inference with common frameworks.

**Scalability testing:** Systems are tested in multi-GPU and multi-node configurations to ensure they scale properly. AI workloads often require dozens or hundreds of GPUs, so scalability is essential.

**Security testing:** Systems are tested for security vulnerabilities and compliance with enterprise security standards. This includes verifying secure boot, encrypted storage, and network security.

#### Program benefits

The certification process benefits NVIDIA in several ways:

**Standardization:** OEMs must design systems to NVIDIA specifications. This ensures consistent quality across vendors. A customer buying from Dell, HPE, Lenovo, or Supermicro gets a consistent experience.

**Switching costs:** Once a vendor has invested in NVIDIA-certified system design, shifting to a competing GPU platform requires redesigning the entire product line. This creates lock-in.

**Quality control:** Certification ensures that systems meet NVIDIA's quality standards. Poor systems would reflect badly on NVIDIA even if NVIDIA didn't manufacture them. Certification protects NVIDIA's brand.

**Channel enablement:** Certification makes it easier for OEMs to sell AI infrastructure. Rather than explaining why their systems are suitable for AI, they can point to NVIDIA certification. This increases sales.

### MGX Reference Architecture

The MGX modular reference architecture enables partners to build accelerated data center servers more quickly. MGX provides a standardized design for GPU servers that supports multiple NVIDIA GPU generations. This reduces the engineering burden on OEMs and accelerates time-to-market for new systems.

#### Modularity benefits

MGX's modular design offers several advantages:

**Faster design:** OEMs can use MGX as a starting point rather than designing from scratch. This reduces engineering time from months to weeks.

**Flexibility:** MGX supports different GPU counts, CPU options, and networking configurations. OEMs can customize systems for different market segments while using common components.

**Upgrade path:** MGX is designed to support multiple GPU generations. When NVIDIA releases a new GPU, OEMs can update MGX designs rather than starting over.

**Economies of scale:** Standardization allows OEMs to achieve economies of scale across product lines. Common components reduce inventory costs and simplify manufacturing.

#### Strategic value

For NVIDIA, MGX ensures that OEM products are optimized for NVIDIA GPUs rather than generic designs. When OEMs use MGX, they are building systems according to NVIDIA's specifications, which maximizes GPU performance and compatibility. This reduces the risk that OEMs will build systems optimized for competing products.

MGX also creates switching costs. Once an OEM has designed products using MGX, shifting to a competing GPU platform requires redesigning the entire product line. The investment in MGX creates an incentive to stay with NVIDIA.

### The Partner Ecosystem Dynamics

The OEM partner relationship has nuances. These server vendors also sell AMD-based systems. They have incentive to support alternative platforms to avoid dependence on a single supplier. But NVIDIA's market dominance makes certified NVIDIA systems far more important to their business than AMD systems. The economic alignment favors NVIDIA.

#### Vendor by vendor

**Dell Technologies:** Dell is the largest server vendor globally by revenue. Dell's PowerEdge XE family of AI servers use NVIDIA GPUs. Dell has embraced NVIDIA-certified systems and offers a wide range of NVIDIA-based products. The relationship is strategically important for both companies.

**Hewlett Packard Enterprise:** HPE is a major enterprise server vendor. HPE's Cray EX supercomputers use NVIDIA GPUs. HPE has partnered with NVIDIA on enterprise AI solutions. The companies collaborate on go-to-market for enterprise customers.

**Lenovo:** Lenovo is a major server vendor particularly strong in Asia. Lenovo's ThinkSystem servers include NVIDIA-based configurations. Lenovo has been aggressive in adopting NVIDIA's latest technologies, including being early to market with Blackwell-based systems.

**Supermicro:** Supermicro has become one of the largest server vendors for AI infrastructure. The company specializes in high-density GPU servers optimized for AI workloads. Supermicro's stock performance has been highly correlated with NVIDIA GPU demand, reflecting the company's dependence on NVIDIA.

#### Channel conflict

Channel conflict represents a risk in NVIDIA's OEM relationships. NVIDIA's DGX systems, which are sold directly by NVIDIA, compete with OEM offerings. DGX systems are premium products with premium pricing, while OEM systems are more standardized and price-competitive.

NVIDIA manages this channel conflict by positioning DGX for customers who want the absolute best performance and are willing to pay for it, while OEM systems serve customers who need good performance at better prices. This segmentation reduces but does not eliminate channel tension.

## Networking and Infrastructure Partners

NVIDIA's full-stack approach extends to networking. The company provides both InfiniBand and Ethernet networking solutions for AI clusters. The Quantum InfiniBand platform targets high-performance networking for supercomputers and AI data centers. The Spectrum-X Ethernet platform optimizes Ethernet performance for AI training, inference, and fine-tuning.

### CoreWeave and Specialized AI Cloud Providers

NVIDIA strengthened collaboration with CoreWeave to accelerate the buildout of more than 5 gigawatts of AI factories by 2030. CoreWeave is a specialized cloud provider for GPU workloads. Unlike general-purpose hyperscalers, CoreWeave focuses exclusively on GPU-accelerated computing. This specialization allows the company to optimize its infrastructure for AI workloads.

#### Specialized provider advantages

Specialized GPU cloud providers like CoreWeave, Lambda Labs, and Voltage Park have advantages over general-purpose hyperscalers:

**Optimization:** Everything about these providers is optimized for GPU workloads. The facility design, power distribution, cooling systems, and software stack are all designed for GPUs rather than general-purpose computing.

**Expertise:** These providers have deep GPU expertise. Their staff understands GPU architecture, CUDA programming, and AI workloads. This expertise translates to better support for customers.

**Flexibility:** Specialized providers can be more flexible than hyperscalers. They can offer custom configurations, unusual contract terms, and specialized services that hyperscalers cannot provide economically.

**Cost efficiency:** By focusing exclusively on GPU workloads, specialized providers can achieve better cost efficiency than hyperscalers that must support diverse workloads.

#### Strategic value

For NVIDIA, specialized providers create alternative channels for NVIDIA GPUs. This reduces customer concentration risk among the top five hyperscalers. If Microsoft Azure, Google Cloud, or AWS reduces NVIDIA purchasing, CoreWeave and similar providers can absorb some of that demand.

The CoreWeave partnership is strategically important. CoreWeave has raised billions in capital to build GPU infrastructure. The company is one of the fastest-growing cloud providers, with revenue growing over 1,000% year-over-year. This growth creates additional demand for NVIDIA GPUs.

The 5-gigawatt target by 2030 is enormous. A typical data center might have 50-100 megawatts of power capacity. 5 gigawatts is 50-100 large data centers dedicated to AI. This commitment demonstrates the scale of AI infrastructure build-out and CoreWeave's ambition to capture a meaningful portion of this market.

### BlueField DPUs and Inference Context Memory

NVIDIA introduced a new product category with the Inference Context Memory Storage Platform, powered by BlueField-4 DPUs (data processing units). This addresses a critical bottleneck in AI inference: the memory bandwidth required for large language model context. The platform extends GPU memory through network-attached storage, reducing the GPU memory capacity required for inference deployments.

#### The context memory bottleneck

Large language models require substantial memory to store model weights. Inference also requires memory for context, the conversation history and other information that the model uses to generate responses. As context windows grow (from 4,000 tokens to 128,000 tokens and beyond), the memory requirements increase.

GPUs have limited memory capacity. H100 GPUs typically have 80 GB of memory. Blackwell GPUs have more, but still limited relative to the demands of large context windows. Loading model weights and context into GPU memory is a bottleneck for inference.

#### BlueField solution

The Inference Context Memory Storage Platform uses BlueField DPUs to extend GPU memory through network-attached storage. Rather than loading all context into GPU memory, less frequently accessed data can reside in network-attached storage and be retrieved as needed. This reduces GPU memory requirements and lowers inference costs.

This product category expansion is significant for several reasons:

**New revenue stream:** It creates a new revenue stream beyond GPUs. BlueField DPUs and associated software provide attach revenue per GPU deployment.

**Attach rate:** It increases NVIDIA's attach rate per GPU deployment. Each GPU deployment can now include not just the GPU but also BlueField DPUs and networking.

**Switching costs:** It creates switching costs by creating an integrated memory and compute solution. Customers using NVIDIA's context memory solution are more locked into NVIDIA GPUs.

**Problem-solving:** It demonstrates NVIDIA's ability to identify and solve AI infrastructure bottlenecks beyond raw compute. This problem-solving capability strengthens NVIDIA's position as a full-stack infrastructure provider.

## Customer Retention and Revenue Dynamics

NVIDIA benefits from strong revenue retention due to several factors. Multi-generational partnerships with customers like Meta create locked-in demand. Increasing AI compute demands as models grow drive natural expansion. Platform stickiness from the CUDA ecosystem creates switching costs. Software subscriptions like NVIDIA AI Enterprise provide recurring revenue.

### The Net Revenue Retention Engine

While NVIDIA does not disclose net dollar retention rates publicly, the dynamics suggest strong retention. Several factors drive retention:

**Technology leadership:** Customers who purchase H100 GPUs for model training typically need to upgrade to Blackwell or Rubin for competitive training. The software stack remains consistent across generations, creating an upgrade path rather than a replacement decision.

**Data gravity:** Training data and model checkpoints accumulated on NVIDIA infrastructure create data gravity. Moving petabytes of data and terabytes of model checkpoints to alternative infrastructure is expensive and risky. Customers tend to stay where their data already lives.

**Staff expertise:** AI engineers and researchers develop expertise with NVIDIA platforms. Rewriting CUDA code and learning new platforms requires retraining staff. This expertise creates resistance to switching.

**Investment protection:** Customers who have invested in NVIDIA infrastructure want to protect that investment. Switching would mean abandoning previous investments, which is difficult to justify unless the alternative is dramatically better.

**Multi-year commitments:** Many customers have signed multi-year commitments for GPU capacity. These contracts create guaranteed revenue for NVIDIA and make switching contractually difficult.

### Churn Risk Factors

Potential churn drivers include:

**Hyperscaler vertical integration:** Hyperscalers developing custom accelerators may reduce NVIDIA purchasing over time. The question is how far they will push custom silicon.

**Competitive pressure:** AMD MI300X and future products, Intel Gaudi, and startup competitors may capture some workloads. If AMD achieves performance parity at lower prices, customers may switch.

**Customer-specific capex timing shifts:** Hyperscalers and enterprises may moderate AI infrastructure spending due to economic conditions, ROI concerns, or strategic shifts. A spending pause would impact NVIDIA even if customers don't switch to competitors.

The mitigating factors include NVIDIA's performance leadership, CUDA ecosystem moat, full-stack solution, and rapid innovation pace. A customer switching to AMD MI300X to save money must accept performance uncertainty, software compatibility issues, and the risk of falling behind competitors who use NVIDIA's latest GPUs. The risk-benefit calculus usually favors staying with NVIDIA.

## Regional Customer Distribution

NVIDIA's customer base is global but concentrated in certain regions. North America represents 45 to 50 percent of demand, driven by hyperscaler presence and AI company concentration. Asia-Pacific outside China represents 10 to 15 percent, with India as a growth market and Japan, Southeast Asia, and Australia as established markets. Europe, Middle East, and Africa account for 15 to 20 percent, with sovereign AI initiatives and automotive partnerships driving demand.

### China: The Constrained Market

China represents 20 to 25 percent of global AI accelerator demand, but NVIDIA's ability to serve this market is constrained by export restrictions. The October 2022 restrictions banned A100 and H100 sales. The October 2023 restrictions banned A800, H800, L40S, and RTX 4090 sales. The H20 chip introduced in 2024 was a compromised product with reduced capabilities. In 2025, China directed domestic companies against purchasing H20, and NVIDIA halted production.

The net effect is that China's AI accelerator market is shifting to domestic alternatives, primarily Huawei Ascend. This represents a permanent loss of 15 to 20 percent of NVIDIA's potential revenue. The company may maintain some presence with compliant products, but the days of selling cutting-edge GPUs to China are likely over.

### North America: The Core Market

North America remains NVIDIA's core market. The hyperscalers are all headquartered in the United States. The leading AI companies are primarily American. The enterprise AI adoption wave is strongest in the United States. Government partnerships, such as the U.S. Department of Energy Genesis Mission, create additional demand. North America's share of NVIDIA revenue may increase as China declines.

## Customer Contract Structure

NVIDIA has multiyear, multigenerational agreements with major customers. The Meta partnership explicitly spans multiple GPU generations. Hyperscalers have long-term supply commitments. OEM partners have multiyear certification and integration agreements. These contract structures create revenue visibility and reduce customer churn risk.

### Forward Purchase Commitments

While NVIDIA does not publicly disclose specific numbers, the company's largest customers have significant forward purchase commitments for GPU deployments. These commitments take various forms, including supply agreements, capacity reservations, and roadmap collaboration. The company's backlog and visibility benefit from these long-term relationships.

The strategic importance of these commitments cannot be overstated. In a market where GPU supply has been constrained, having a guaranteed allocation is valuable. Customers willing to make multiyear commitments get priority access to the latest GPUs. This creates a virtuous cycle: the best customers get the best GPUs, which makes them more competitive, which increases their purchasing power, which reinforces their priority status.

## The Customer Concentration Risk

NVIDIA's customer concentration is both a strength and vulnerability. The strength is the scale and predictability that come from large, committed customers. The vulnerability is the leverage these customers have in negotiations and their motivation to develop alternatives.

### Hyperscaler Leverage

The hyperscalers have engineering resources to develop custom accelerators, financial scale to fund multi-billion dollar silicon programs, and strategic motivation to reduce NVIDIA dependence. Each has implemented custom silicon to some degree. The question is how far they will push this strategy.

The current evidence suggests a hybrid approach rather than full displacement. Hyperscalers use custom silicon for 30 to 40 percent of workloads and NVIDIA for 60 to 70 percent. The NVIDIA portion is the cutting-edge training segment where margins are highest. The custom silicon portion is the inference and stable workload segment where margins are lower. This outcome is manageable for NVIDIA.

### Diversification Progress

NVIDIA is gradually diversifying its customer base. Enterprise AI adoption is creating a new customer segment beyond hyperscalers. Sovereign AI projects are creating national-scale customers. Automotive and healthcare verticals are scaling. Regional diversification into India, Japan, and international markets reduces concentration in any single geography.

The diversification is real but gradual. Hyperscalers will remain the largest customer segment for the foreseeable future. The question is whether their share of NVIDIA revenue will decline from 50 percent to perhaps 35 to 40 percent as other segments grow. This is a plausible outcome over the next five years.

## Use Case Evolution: From Training to Inference to Agents

The use cases driving NVIDIA GPU demand are evolving. The initial wave was AI training for foundation models. The current wave is AI inference for generative AI services. The emerging wave is agentic AI, where AI systems can reason, plan, and take actions autonomously. NVIDIA's infrastructure must serve all three waves.

### Generative AI and LLM Training

Training foundation models remains the primary use case for NVIDIA's highest-end GPUs. GPT-4, Llama 3, Claude 3, and other frontier models required tens of thousands of GPUs running for months. The training cost for GPT-4 was estimated at over 100 million dollars in compute. The training cost for Llama 3 405B was similarly enormous. These training runs create demand for H100, H200, and Blackwell GPUs.

### Inference Scaling

Inference represents a growing portion of AI compute spend. ChatGPT serves hundreds of millions of users, each query requiring inference compute. The cumulative inference cost exceeds the training cost within months of deployment. NVIDIA's inference optimization, including TensorRT and transformer engines, reduces the cost per token. The Inference Context Memory Storage Platform extends GPU memory for larger context windows.

### Agentic AI Emergence

Agentic AI represents the emerging use case. Agents are AI systems that can reason, plan, and execute complex workflows autonomously. NVIDIA's Nemotron 3 family of open models targets agentic AI. CEO Jensen Huang has stated that "enterprise adoption of agents is skyrocketing." Agentic AI requires different optimization than chatbot-style AI. It emphasizes reasoning quality, context management, and reliable execution rather than merely fast token generation.

### Physical AI and Robotics

Physical AI for robotics and autonomous machines is a distinct use case with different requirements. Real-time sensor processing, precise control, and edge deployment are critical. NVIDIA's Isaac platform, Jetson edge AI hardware, and partnerships with robotics companies target this segment. The opportunity is complementary to data center AI. Physical AI deployments require both training in data centers and inference at the edge.

## Strategic Assessment of the Customer Ecosystem

NVIDIA's customer ecosystem is the foundation of its business model. The company sells to the world's most valuable organizations, from hyperscalers with trillion-dollar market caps to sovereign nations with multi-billion dollar AI initiatives. The customer relationships are deep, multi-generational, and strategically significant.

The strength of the customer ecosystem is evident in the financial results. Data Center revenue of 193.7 billion dollars in fiscal 2026 demonstrates the scale of customer demand. The growth rate of 68 percent year-over-year demonstrates the momentum. The gross margins above 75 percent demonstrate the pricing power that comes from customer dependency.

The vulnerability is equally evident. Customer concentration among a small number of hyperscalers creates dependency. Those customers are developing custom alternatives. China, a major market, is effectively lost due to export restrictions. Enterprise AI adoption, while promising, is still early compared to hyperscaler demand.

The most likely outcome is gradual diversification rather than sudden disruption. Hyperscalers will remain the largest customer segment but will reduce their relative share as enterprises, sovereign AI projects, and vertical markets grow. Custom silicon will capture some workloads but NVIDIA will retain the cutting-edge training segment where margins are highest. China will transition to domestic alternatives, but North America, India, Europe, and other markets will compensate.

For NVIDIA investors, the customer ecosystem analysis supports a nuanced view. The company is not a single-customer dependency story like some enterprise software companies. It is not a diversified consumer business with millions of customers. It is a concentrated business with deep, strategic relationships to a small number of enormous customers. The durability of these relationships depends on NVIDIA maintaining its technology leadership and the economic value of AI compute exceeding the cost of custom silicon development.
