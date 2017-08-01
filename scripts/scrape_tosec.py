from classes.tosec_scraper import *

if __name__=='__main__':
    ts = TOSECScraper(cache=False)
    ts.paths = ts.generateTOSECPathsArrayFromDatFiles()
    ts.db.loadCache()
    ts.scrapeTOSEC()
    ts.updateTOSECAliasesCSV()
    ts.addUnscraped()
    ts.db.commit()
    # with open('tosec_inconsistencies.csv', 'w', encoding='utf-8') as f:
    #     for array in ts.wrong_releases:
    #         f.write(';'.join(array)+'\n')
    #     for array in ts.inconsistencies:
    #         f.write(';'.join(array)+'\n')
