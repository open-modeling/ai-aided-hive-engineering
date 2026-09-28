# Figure 9-1 rendering prompt

## Purpose

Render **Figure 9-1 - Scale, Magnification Bands, and topology-preserving engineering flow** for the AI Aided Hive Engineering Proposal.

The figure is an Illustration of §9. It must not introduce model semantics or implementation bindings beyond the proposal text.

## Geometry

Depict the formal engineering projection as a rectangular structure with:

- Engineering Domains on the horizontal direction;
- the common ordered Scale on the vertical direction.

Domains are sparse. Do not draw mandatory Layer cells at every Scale position.

Show the underlying engineering graph as capable of richer internal structure than the rectangular projection.

Optionally include a small inset that wraps the Domain direction around a cylinder. The cylinder is explanatory only. Do not imply cyclic Domain adjacency or semantic meaning from angular distance.

## Magnification Bands

Engineering Layers are graph nodes with Magnification Bands.

Show both:

- point Bands, represented as A{2};
- non-zero free-floating Bands, represented as C[1-3].

A non-zero Band is normal.

Show Layer-bound semantic content moving with the same Band as its Layer. Do not show one valid Layer containing bound Propositions at different Magnification points.

Include an explicitly rejected Magnification Conflict with L1[2-3], p1{2} bound to L1, and p2{3} bound to L1. Mark the affected continuation as blocked until the conflict is resolved.

## Band alignment and compaction

Show C[1-3], B[2-3], their overlap [2-3], governed compaction C[1-3] -> C[2-3], and the resulting valid same-Band cross-Domain relation C[2-3] <-> B[2-3].

Do not collapse either Layer to a point unless another valid constraint requires that point.

Compaction must visibly preserve node identity and must not appear as a graph-node merge.

## Rectangularity

Horizontal direct cross-Domain relations connect equal Bands only.

Vertical Scale propagation stays inside one Domain and crosses only adjacent Engineering Layer boundaries.

Show a diagonal cross-Domain/cross-Band relation as explicitly rejected.

Show a Layer-skipping vertical relation as explicitly rejected.

## No-fold merge example

Show A{2} <-> B{2} and A{3} <-> B{3}.

Then show the attempted merge A{2}+A{3} -> A[2-3] as rejected while both external relations remain.

Do not depict B{2} and B{3} as collapsing merely because Domain A attempted a merge.

Do not silently delete either external relation.

## Human locality

A Human can be drawn with an applicability Band represented as Human[2-3].

Show possible participation at a Layer {3} inside that Band.

Do not show the Human Band as authority, and do not collapse Human[2-3] to {3} merely because one participation occurs at {3}.

## Exchange Items

Use one Exchange Item identity for one governed transfer.

Vertical transfer is Domain-local and crosses only adjacent Engineering Layers.

Horizontal cross-Domain transfer occurs only between equal Bands.

A single Exchange Item must not simultaneously change Domain and Magnification Band.

Where both operations are required, show separate governed transitions with receiving-layer decomposition into locally addressable semantic state.

## Decision propagation

Show a Decision Candidate with calculated Decision Blast Radius over the valid topology and a committed Decision with separate Decision Extent.

Neither region overrides Band, adjacency, or no-diagonal rules.

## Visual restrictions

Do not imply:

- fixed universal Layer names;
- mandatory dense Domain grids;
- non-zero Band as an anomaly;
- valid Layer-bound content with unequal Bands;
- diagonal engineering relations;
- Layer-skipping propagation;
- graph contraction as Band compaction;
- local Layer merge collapsing related Layers in other Domains;
- Human Magnification applicability as Authority;
- Magnification-generated detail;
- Decision Blast Radius as a Euclidean sphere.
