describe("paragraph", function () {
  var p = document.getElementsByTagName("p")[0];

  it("should exist", function () {
    expect(p).toBeDefined();
  });

  it('should show "Hello, World!" on the screen', function () {
    var content = p.textContent.trim();
    expect(content).toEqual("Hello, world!");
  });

  it('should have a class of "body"', function () {
    expect(p.className).toEqual("body");
  });
});
