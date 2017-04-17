/**
 * Copyright 2017 Nidium Inc. All rights reserved.
 * Use of this source code is governed by a MIT license
 * that can be found in the LICENSE file.
 */

{
    const Elements = require("Elements");

    Elements.div = class extends Elements.Element {
        constructor(attributes) {
            super(attributes);
        }

        paint(ctx) {
            super.paint(ctx)
        }
    }
}