/** @odoo-module **/

import publicWidget from 'web.public.widget';
import {generateGMapLink, generateGMapIframe} from 'website.utils';

publicWidget.registry.blog = publicWidget.Widget.extend({
    selector: '.blogsection',

    /**
     * @override
     */
    start() {
        console.log("Hello word blog qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")

        let card = this.el.querySelector('#list')

        if (card) {
            let html = ``
            this._rpc({
                route: '/get-blog/',
                params: {}

            }).then(data => {

                console.log('Data:', data)

                data.forEach(entry => {
                    console.log('Response:', entry)

                    html += `<div class="items">

                                        <div class="contents">
                                            <img src="${entry.image}"
                                                 alt="" loading="lazy"/>
                                            <div class="pintura" ">
                                                <p style="color: white"> ${entry.post_title}</p>

                                            </div>

                                        </div>
                                    </div>`

                })
                    card.innerHTML = html
            })

        }

    },
});

export default publicWidget.registry.blog;