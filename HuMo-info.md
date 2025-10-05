# HuMO

When using `HuMo` safetensors it may be possible to use `WanVideo Long I2V Multi/InfiniteTalk` in addition to or instead of `HuMo Embeds`.
If both are used at the same time the embeds need to do be mixed using `WanVideo Combine Embeds`.
In this case `HuMo Embeds` is plugged first and `WanVideo Long I2V Multi/InfiniteTalk` is plugged second.
`WanVideo Long I2V Multi/InfiniteTalk` in this scenario controls looping like for a regular `InfiniteTalk` generation.
It looks like `WanVideo Long I2V Multi/InfiniteTalk` additionally makes `HuMo` model respect the start frame more strongly.

`HuMo` might work with other I2V workflows as well.

It appears difficult to stop characters opening their mouth with `HuMO` (though one can try with silent audio).

Without `WanVideo Long I2V Multi/InifiniteTalk` node `HuMo` is limited to less than 4 seconds of generation.

It appears `HuMo` can use multiple reference images.