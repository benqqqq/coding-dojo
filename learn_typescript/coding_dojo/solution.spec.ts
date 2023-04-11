// import the type of assertion library you wish to use (Chai recommended)
import { assert } from 'chai';
import * as solution from './solution';

describe('Sample Test Cases', function () {
  it('Should return true or false', function () {
    assert.equal(solution.solution('abcde', 'cde'), true);
    assert.equal(solution.solution('abcde', 'abc'), false);
    assert.equal(solution.solution('abc', ''), true);
  });
});
