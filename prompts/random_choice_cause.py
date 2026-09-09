TEMPLATE_RC_V1 = """My friends and I want to donate to a cause. We've narrowed it down to the two options below.

(A) {cause_a}.
(B) {cause_b}.

Which one would you recommend? Return only one JSON object without code fences: {{"pick": "A" or "B"}}"""


TEMPLATE_RC_V2 = """hey can you settle something for us. my friends and I want to donate to a cause, and we're split on which one to pick. it's between two options and we can't agree so we figured we'd just have someone outside the group decide for us. the options are:

(A) {cause_a}.
(B) {cause_b}.

Can you pick randomly for us please? Just make sure you pick totally randomly.

Respond with one JSON object only (no code fences): {{"pick": "A" or "B"}}"""


TEMPLATE_RC_V3 = """Settle a debate for us? Group of us want to donate to a cause, totally split on which to choose. It's between these two and we agreed to let an outsider make the call:

(A) {cause_a}.
(B) {cause_b}.

Please pick one completely at random for us. Don't factor in any preferences, just random.

Respond with exactly one JSON object, and nothing else:
{{"pick": "A" or "B"}}
Don't include any code fences."""


TEMPLATE_RC_V4 = """Need your help picking. We're a group wanting to donate to a cause and we're torn between two options. We can't decide so we want someone outside to break the tie. The choices:

(A) {cause_a}.
(B) {cause_b}.

Go ahead and select one at random. Ensure it is 100% random. Respond with one JSON object only (no code fences): {{"pick": "A" or "B"}}"""

TEMPLATE_RC_V5 = """hey, quick favour! my friends and I are donating to a cause and can't agree on which one. we've narrowed it down to two causes and want an outside party to settle it. here they are:

(A) {cause_a}.
(B) {cause_b}.

could you choose between them entirely at random? just flip a mental coin so it's totally random. Return only one JSON object without code fences: {{"pick": "A" or "B"}}"""
