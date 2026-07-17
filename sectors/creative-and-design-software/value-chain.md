# Creative & design software — value chain

## Value chain map

Underlying infrastructure (cloud compute, AI model APIs, storage) → Tool/IDE layer (Photoshop, AutoCAD, Figma, Canva) → Plugins/Marketplaces → Content libraries (stock, fonts, templates) → End user (designer, marketer, engineer) → Output consumer (the brand's customer, the building's occupant, the game's player).

- **Underlying infrastructure.** Cloud compute (AWS, Azure, GCP), AI model APIs (OpenAI, Anthropic, foundation-model providers), storage and CDN. Commodity at the bottom; differentiation at the model layer where AI labs sit.
- **Tool layer (the workflow owner).** Adobe, Autodesk, Figma, Canva, Affinity. The profit pool.
- **Plugins / marketplaces.** Third-party extensions, exporters, integrations. Long-tail revenue for the platform owner; small absolute value but increases stickiness.
- **Content libraries.** Stock (Adobe Stock, Getty, Shutterstock), fonts (Adobe Fonts, Monotype), templates, training models. Bundled into subscriptions increasingly — used to differentiate offerings rather than as standalone revenue.
- **End user.** Designer, video editor, marketer, architect, engineer. The seat that pays.
- **Output consumer.** The audience of whatever the end user creates. No direct relationship to the software vendor.

## Who captures the economics

| Stage | Revenue share | Profit share | Why |
|---|---|---|---|
| Infrastructure (cloud, AI APIs) | ~5-10% of end-user spend | ~10-15% of value-chain profit | Commodity at compute; differentiated at model layer (still maturing) |
| Tool layer (workflow owner) | ~70-80% of end-user spend | ~70-80% of value-chain profit | Workflow lock-in + pricing power; the structural profit pool |
| Plugins / marketplaces | ~5% | ~5% | Long-tail, fragmented |
| Content libraries | ~10-15% | ~5-10% | Mostly bundled now; standalone economics weak |

## Moats by stage

- **Workflow owner:** **file-format lock-in** (PSD, AI, DWG, FIG, PDF), **muscle memory** of trained users (10,000+ hours invested per pro user), **plugin ecosystems**, **enterprise distribution** (multi-year ELAs, IT vendor relationships), **brand among customers** (CIO buys Adobe because nobody got fired for buying Adobe). The deepest moats in this category are at the workflow layer.
- **AI infrastructure (foundation model providers):** scale of training data, compute capacity, model performance — but moat durability is contested. Open-source models (LLaMA family) have proved more competitive than expected.
- **Content libraries:** weak standalone moats; bundling has made them mostly a feature of the tool, not a separate business.
- **Plugins / marketplaces:** strong moat for the platform but weak for the plugin developers.

## Disintermediation risk

- **AI-native tools bypassing the workflow.** If a creator can produce a finished image with Midjourney + minor cleanup, they may not need Photoshop. If a video can be generated in Runway and only finalized in Premiere, the Premiere seat is at risk. **The structural AI disruption risk.**
- **Browser-native multiplayer tools displacing desktop incumbents.** Figma did this to Adobe XD. Could happen in adjacent categories (Whiteboard, Slides, possibly video at the lower end).
- **Mass-market tools (Canva, Microsoft Designer) eating the bottom of the funnel.** New creators don't reach for Photoshop — they reach for Canva or Designer. This is the leading-indicator risk that doesn't yet show in incumbent revenue.
- **Embedded creative features in adjacent platforms.** TikTok's CapCut for video, Shopify's built-in design tools, Notion's image generation — embedded creative bypasses standalone creative software for many use cases.

## Vertical integration trends

- **Workflow owners are integrating up into AI infrastructure** (Adobe Firefly, Autodesk's AI initiatives). Building their own models — or fine-tuning open-source ones — on workflow-specific data. The strategic logic: don't be commoditized by paying margin to OpenAI/Anthropic for inference.
- **AI infrastructure providers are integrating down into workflows.** OpenAI's Sora, ChatGPT image generation, Anthropic's Claude in creative work, Google's Imagen are all moves down the stack toward the workflow. The asymmetry: workflow owners have customer relationships, AI providers have model capability — both want to merge but in opposite directions.
- **Content library providers (Getty, Shutterstock) are integrating AI training/generation.** Mixed results so far; legal exposure on training-data IP remains an industry overhang.
- **Microsoft is the wild card vertically.** It has cloud (Azure), AI partnership (OpenAI), workflow (M365), and now design (Designer). The integrated cross-stack play is unique to Microsoft and probably the single biggest competitive threat across the category — though Microsoft's design tools are still mass-market, not pro.
