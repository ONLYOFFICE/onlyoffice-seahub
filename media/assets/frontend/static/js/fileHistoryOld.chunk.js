(this["webpackJsonpseahub-frontend"]=this["webpackJsonpseahub-frontend"]||[]).push([[7],{1069:function(t,e,a){t.exports=a(1295)},1070:function(t,e,a){},1295:function(t,e,a){"use strict";a.r(e);var i=a(58),s=a(6),n=a(7),o=a(9),r=a(8),c=a(2),d=a.n(c),l=a(24),h=a.n(l),j=a(4),b=a(5),m=a(10),O=a(1),u=a(84),f=a(16),p=a(76),g=a(46),x=a(13),v=a.n(x),w=a(79),R=a(0);v.a.locale(window.app.config.lang);var y=function(t){Object(o.a)(a,t);var e=Object(r.a)(a);function a(t){var i;return Object(s.a)(this,a),(i=e.call(this,t)).onMouseEnter=function(){i.setState({active:!0})},i.onMouseLeave=function(){i.setState({active:!1})},i.onItemRestore=function(t){t.preventDefault(),i.props.onItemRestore(i.props.item)},i.state={active:!1},i}return Object(n.a)(a,[{key:"render",value:function(){var t=this.props.item,e=w.a.getUrl({type:"download_historic_file",filePath:O.jb,objID:t.rev_file_id}),a="".concat(O.lc,"profile/").concat(encodeURIComponent(t.creator_email),"/"),i="".concat(O.lc,"repo/").concat(O.rb,"/history/files/?obj_id=").concat(t.rev_file_id,"&commit_id=").concat(t.commit_id,"&p=").concat(O.jb),s="".concat(O.lc,"repo/text_diff/").concat(O.rb,"/?commit=").concat(t.commit_id,"&p=").concat(O.jb);return Object(R.jsx)(c.Fragment,{children:Object(R.jsxs)("tr",{onMouseEnter:this.onMouseEnter,onMouseLeave:this.onMouseLeave,className:this.state.active?"tr-highlight":"",children:[Object(R.jsxs)("td",{children:[Object(R.jsx)("time",{datetime:t.time,is:"relative-time",title:v()(t.ctime).format("llll"),children:v()(t.ctime).fromNow()}),0===this.props.index&&Object(O.nb)("(current version)")]}),Object(R.jsxs)("td",{children:[Object(R.jsx)("img",{className:"avatar",src:t.creator_avatar_url,alt:""})," ",Object(R.jsx)("a",{href:a,target:"_blank",className:"username",children:t.creator_name})]}),Object(R.jsx)("td",{children:b.a.bytesToSize(t.size)}),Object(R.jsx)("td",{children:this.state.active&&Object(R.jsx)(_,{index:this.props.index,downloadUrl:e,viewUrl:i,diffUrl:s,onItemRestore:this.onItemRestore,canDownload:this.props.canDownload,canCompare:this.props.canCompare})})]})})}}]),a}(d.a.Component),_=function(t){Object(o.a)(a,t);var e=Object(r.a)(a);function a(t){var i;return Object(s.a)(this,a),(i=e.call(this,t)).dropdownToggle=function(){i.setState({dropdownOpen:!i.state.dropdownOpen})},i.state={dropdownOpen:!1},i}return Object(n.a)(a,[{key:"render",value:function(){var t=this.props,e=t.index,a=t.downloadUrl,i=t.viewUrl,s=(t.diffUrl,t.onItemRestore),n=(t.canCompare,t.canDownload);return Object(R.jsxs)(j.l,{isOpen:this.state.dropdownOpen,toggle:this.dropdownToggle,direction:"down",className:"mx-1 old-history-more-operation",children:[Object(R.jsx)(j.o,{tag:"i",className:"fa fa-ellipsis-v",title:Object(O.nb)("More Operations"),"data-toggle":"dropdown","aria-expanded":this.state.dropdownOpen}),Object(R.jsxs)(j.n,{className:"drop-list",right:!0,children:[0!==e&&Object(R.jsx)("a",{href:"#",onClick:s,children:Object(R.jsx)(j.m,{children:Object(O.nb)("Restore")})}),n&&Object(R.jsx)("a",{href:a,children:Object(R.jsx)(j.m,{children:Object(O.nb)("Download")})}),Object(R.jsx)("a",{href:i,children:Object(R.jsx)(j.m,{children:Object(O.nb)("View")})})]})]})}}]),a}(d.a.PureComponent),L=y,S=(a(142),a(99),a(112),a(1070),function(t){Object(o.a)(a,t);var e=Object(r.a)(a);function a(t){var i;return Object(s.a)(this,a),(i=e.call(this,t)).listNewHistoryRecords=function(t,e){u.a.listFileHistoryRecords(t,1,e).then((function(t){if(!t.data)throw i.setState({isLoading:!1}),Error("There is an error in server.");i.initNewRecords(t.data)}))},i.listOldHistoryRecords=function(t,e){m.a.listOldFileHistoryRecords(t,e).then((function(t){if(!t.data)throw i.setState({isLoading:!1}),Error("There is an error in server.");i.initOldRecords(t.data)}))},i.onScrollHandler=function(t){var e=t.target.clientHeight,a=t.target.scrollHeight,s=e+t.target.scrollTop+1>=a,n=i.state.hasMore;s&&n&&i.reloadMore()},i.reloadMore=function(){if(!i.state.isReloadingData)if(O.wc){var t=i.state.currentPage+1;i.setState({currentPage:t,isReloadingData:!0}),u.a.listFileHistoryRecords(O.jb,t,O.a).then((function(t){i.updateNewRecords(t.data)}))}else{var e=i.state.nextCommit,a=i.state.filePath,s=i.state.oldFilePath;i.setState({isReloadingData:!0}),s?m.a.listOldFileHistoryRecords(O.rb,s,e).then((function(t){i.updateOldRecords(t.data,s)})):m.a.listOldFileHistoryRecords(O.rb,a,e).then((function(t){i.updateOldRecords(t.data,a)}))}},i.onItemRestore=function(t){var e=t.commit_id,a=t.path;u.a.revertFile(a,e).then((function(t){t.data.success&&(i.setState({isLoading:!0}),i.refershFileList())}))},i.onSearchedClick=function(t){b.a.handleSearchedItemClick(t)},i.state={historyList:[],currentPage:1,hasMore:!1,nextCommit:void 0,filePath:"",oldFilePath:"",isLoading:!0,isReloadingData:!1},i}return Object(n.a)(a,[{key:"componentDidMount",value:function(){O.wc?this.listNewHistoryRecords(O.jb,O.a):this.listOldHistoryRecords(O.rb,O.jb)}},{key:"initNewRecords",value:function(t){var e=this;if(t.total_count<5)if(t.data.length){var a=t.data[t.data.length-1].commit_id,i=t.data[t.data.length-1].path,s=t.data[t.data.length-1].old_path;i=s||i,m.a.listOldFileHistoryRecords(O.rb,i,a).then((function(a){if(!a.data)throw e.setState({isLoading:!1}),Error("There is an error in server.");e.setState({historyList:t.data.concat(a.data.data.slice(1,a.data.data.length)),isLoading:!1})}))}else m.a.listOldFileHistoryRecords(O.rb,O.jb).then((function(t){if(!t.data)throw e.setState({isLoading:!1}),Error("There is an error in server.");e.setState({historyList:t.data.data,isLoading:!1})}));else this.setState({historyList:t.data,currentPage:t.page,hasMore:t.total_count>O.a*this.state.currentPage,isLoading:!1})}},{key:"initOldRecords",value:function(t){var e=this;t.data.length?this.setState({historyList:t.data,nextCommit:t.next_start_commit,filePath:t.data[t.data.length-1].path,oldFilePath:t.data[t.data.length-1].rev_renamed_old_path,isLoading:!1}):(this.setState({nextCommit:t.next_start_commit}),this.state.nextCommit?m.a.listOldFileHistoryRecords(O.rb,O.jb,this.state.nextCommit).then((function(t){e.initOldRecords(t.data)})):this.setState({isLoading:!1}))}},{key:"updateNewRecords",value:function(t){this.setState({historyList:[].concat(Object(i.a)(this.state.historyList),Object(i.a)(t.data)),currentPage:t.page,hasMore:t.total_count>O.a*this.state.currentPage,isReloadingData:!1})}},{key:"updateOldRecords",value:function(t,e){var a=this;t.data.length?this.setState({historyList:[].concat(Object(i.a)(this.state.historyList),Object(i.a)(t.data)),nextCommit:t.next_start_commit,filePath:t.data[t.data.length-1].path,oldFilePath:t.data[t.data.length-1].rev_renamed_old_path,isReloadingData:!1}):(this.setState({nextCommit:t.next_start_commit}),this.state.nextCommit&&m.a.listOldFileHistoryRecords(O.rb,e,this.state.nextCommit).then((function(t){a.updateOldRecords(t.data,e)})))}},{key:"refershFileList",value:function(){var t=this;O.wc?u.a.listFileHistoryRecords(O.jb,1,O.a).then((function(e){t.initNewRecords(e.data)})):m.a.listOldFileHistoryRecords(O.rb,O.jb).then((function(e){t.initOldRecords(e.data)}))}},{key:"render",value:function(){var t=this;return Object(R.jsxs)(c.Fragment,{children:[Object(R.jsxs)("div",{id:"header",className:"old-history-header",children:[Object(R.jsx)("div",{className:"logo",children:Object(R.jsx)(p.a,{showCloseSidePanelIcon:!1})}),Object(R.jsx)("div",{className:"toolbar",children:Object(R.jsx)(g.a,{onSearchedClick:this.onSearchedClick})})]}),Object(R.jsx)("div",{id:"main",onScroll:this.onScrollHandler,children:Object(R.jsxs)("div",{className:"old-history-main",children:[Object(R.jsxs)(c.Fragment,{children:[Object(R.jsx)("a",{href:"javascript:window.history.back()",className:"go-back",title:"Back",children:Object(R.jsx)("span",{className:"fas fa-chevron-left"})}),Object(R.jsxs)("h2",{children:[Object(R.jsx)("span",{className:"file-name",children:O.ib})," ",Object(O.nb)("History Versions")]})]}),Object(R.jsxs)(c.Fragment,{children:[Object(R.jsxs)("table",{className:"commit-list",children:[Object(R.jsx)("thead",{children:Object(R.jsxs)("tr",{children:[Object(R.jsx)("th",{width:"40%",children:Object(O.nb)("Time")}),Object(R.jsx)("th",{width:"30%",children:Object(O.nb)("Modifier")}),Object(R.jsx)("th",{width:"25%",children:Object(O.nb)("Size")}),Object(R.jsx)("th",{width:"5%"})]})}),!this.state.isLoading&&Object(R.jsx)("tbody",{children:this.state.historyList.map((function(e,a){return Object(R.jsx)(L,{item:e,index:a,canDownload:O.n,canCompare:O.l,onItemRestore:t.onItemRestore},a)}))})]}),(this.state.isReloadingData||this.state.isLoading)&&Object(R.jsx)(f.a,{}),this.state.nextCommit&&!this.state.isLoading&&!this.state.isReloadingData&&Object(R.jsx)(j.c,{className:"get-more-btn",onClick:this.reloadMore,children:Object(O.nb)("More")})]})]})})]})}}]),a}(d.a.Component));h.a.render(Object(R.jsx)(S,{}),document.getElementById("wrapper"))}},[[1069,1,0]]]);
//# sourceMappingURL=fileHistoryOld.chunk.js.map