import { XanaduFrontendPage } from './app.po';

describe('xanadu-frontend App', () => {
  let page: XanaduFrontendPage;

  beforeEach(() => {
    page = new XanaduFrontendPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
