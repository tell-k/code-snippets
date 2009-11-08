require 'spec_helper'

#User: 投稿アカウントを持つ利用者
describe User, "が、ログインしようとするとき" do
 #前提条件
 before do
  @user = User.find_by_name('example of valid user')
 end
 it "は、正しいログインパスワードでログインできること" do
   @user.login('valid passwrod')
   @user.should be_logged_in
 end 
 it "は、パスワードなしでログインできない事" do
   @user.login(nil)
   @user.should_not be_logged_in
 end
 it "は、間違ったパスワードでログインはできないこと" do
   @user.login("wrong password")
 end
end
