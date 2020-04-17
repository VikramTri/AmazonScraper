

    def singleProductAvailable(self, response):

        productUID = response.meta['productUID']

        mrp = response.xpath('//*[@id="price"]/table/tr[1]/td[2]/span[1]/text()').extract()[0]
        # normalize the MRP to manage unicode characters
        formattedMRP = mrp.replace(u'\u20b9\xa0', '')

        sPrice = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()
        formattedSellingPrice = sPrice.replace(u'\u20b9\xa0', '')

        fulfilledByAMZ = response.xpath('//*[@id="priceblock_ourprice_row"]/td[2]/span[2]').extract()
        if fulfilledByAMZ is None:
            protalVarified = 0
        else:
            protalVarified = 1

        item = AmzProductdetailsItem()

        item['productUID'] = productUID
        item['available'] = 1
        item['avgRating'] = response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()').extract()[0]
        item['totalReviews'] = response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()[0]
        item['mrp'] = formattedMRP
        item['sellingPrice'] = formattedSellingPrice
        item['portalVarified'] = protalVarified
        item['seller'] = response.xpath('//*[@id="sellerProfileTriggerId"]/text()').extract()[0]
        item['size'] = response.xpath('//*[@id="variation_size_name"]/div/span[1]/text()').extract()[0]
        item['productInfo'] = response.xpath('//*[@id="feature-bullets"]').extract()[0]
        item['offers'] = response.xpath('//*[@id="sopp_feature_div"]/ul').extract()[0]
        item['additionalInfo1'] = response.xpath('//*[@id="productDetailsTable"]/tr/td/div/ul/li[1]/text()').extract()[0]
        item['additionalInfo2'] = response.xpath('//*[@id="productDetailsTable"]/tr/td/div/ul/li[4]').extract()[0]
        item['fistSellingDate'] = response.xpath('//*[@id="productDetailsTable"]/tr/td/div/ul/li[2]/text()').extract()[0]
        item['linkToReviews'] = response.xpath('//*[@id="reviews-medley-footer"]/div[2]/a/@href').extract()[0]

        yield item

   